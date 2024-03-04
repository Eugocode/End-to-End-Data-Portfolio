import sys  #used to add parameters when we run scripts/functions
import json #for configuration file
import time #for working with time-related functions
import schedule #schedule execution
import pandas as pd #preprocessing of data
from os import environ, remove #access os environment variables and file deletion
from pathlib import Path #get the actual file system paths
from ftplib import FTP_TLS #to connect to FTP Server

#---------------------------------------------------START OF: Extracting Data from Web to FTP --------------------------------------------------###

# Function to retrieve the authenticated FTP_TLS object
def get_ftp() -> FTP_TLS:
    # Get FTP details
    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]
    FTPPORT = environ["FTPPORT"]

    # Return authenticated FTP object
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp.prot_p()

    print("FTP server running...")

    return ftp 

# Function to upload file to FTP server
def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as fp:
        ftp.storbinary(f"STOR {file_source.name}", fp)

# Function to delete file from local filesystem
def delete_file(file_source: str | Path):
    remove(file_source)

# Function to read CSV data from web url
def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params) #** means that we are decompressing the dictionary and get the actual parameter name

# Main pipeline function for data extraction and upload
def pipeline():
    # Load source configuration
    with open("config.json", "rb") as fp:
        config = json.load(fp)
    
    # Get an authenticated FTP Object
    ftp = get_ftp()

    for source_name, source_config in config.items():
        file_name = Path(source_name + ".csv")
        df = read_csv(source_config)
        df.to_csv(file_name, index=False)

        print(f"File {file_name} has been downloaded.")
        
        upload_to_ftp(ftp, file_name)
        print(f"File {file_name} has been uploaded to FTP.")

        # delete files after upload
        delete_file(file_name)
        print(f"File {file_name} has been deleted.")

### ---------------------------------------------------- END OF: Extracting Data from Web to FTP -----------------------------------------------###

if __name__=="__main__":
    
    # add 2 parameters (manual and schedule) when running the script
    param = sys.argv[1]

    if param=="manual":
        pipeline()

    elif param=="schedule":

        # scheduling to run everyday at a certain time
        schedule.every().day.at("14:18").do(pipeline)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid parameter. The app will not run.")