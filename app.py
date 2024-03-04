import sys  #add parameters when we run script
import json #for configuration file

# schedule execution
import time 
import schedule

# preprocessing of data
import pandas as pd 
# access environment variables
from os import environ, remove 
# get the actual path
from pathlib import Path 
# to connect to FTP Server
from ftplib import FTP_TLS 

def get_ftp() -> FTP_TLS:
    # Get FTP details
    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]
    FTPPORT = environ["FTPPORT"]

    # Return authenticated FTP
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)

    ftp.prot_p()

    print("FTP server running...")

    return ftp 

def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as fp:
        ftp.storbinary(f"STOR {file_source.name}", fp)

def delete_file(file_source: str | Path):
    remove(file_source)

def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params) #** means that we are decompressing the dictionary and get the actual parameter name

def pipeline():
       # Load source configuration
    with open("config.json", "rb") as fp:
        config = json.load(fp)
    
    # Get an authenticated FTP Object
    ftp = get_ftp()

    # print(read_csv(config["OFAC_SDN"]).head())
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

if __name__=="__main__":
    
    param = sys.argv[1]

    if param=="manual":
        pipeline()
        
    elif param=="schedule":

        # scheduling to run at a certain time
        schedule.every().day.at("14:18").do(pipeline)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid parameter. The app will not run.")