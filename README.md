# First End-to-End Data Portfolio

This repository is created as part of the First End-to-End Data Portfolio series of Josh Dev.

Tutorial Playlist: https://youtube.com/playlist?list=PLtomnyC4qhTwqcZ3DzBhewMNjM_4rHqnO&si=vFGy-E1e6FYEjF60

"In this series, the participants will apply their knowledge with 𝗣𝘆𝘁𝗵𝗼𝗻 and 𝗦𝗤𝗟 in building an end-to-end data pipeline. Aside from data engineering skills, they will also wear the data analyst and data scientist hats by building 𝗱𝗮𝘀𝗵𝗯𝗼𝗮𝗿𝗱𝘀, performing 𝗱𝗮𝘁𝗮 𝗮𝗻𝗮𝗹𝘆𝘀𝗶𝘀, and training 𝗺𝗮𝗰𝗵𝗶𝗻𝗲 𝗹𝗲𝗮𝗿𝗻𝗶𝗻𝗴 𝗺𝗼𝗱𝗲𝗹𝘀. This is especially helpful to those who are yet to discover their forte in data." - Josh Dev

## Instructions

1. Clone this repository.
2. Create a virtual environment.
   `python -m venv env`
3. Activate virtual environment.
   - for powershell `.\env\Scripts\Activate.ps1`
   - for cmd `.\env\Scripts\activate.bat`
4. Install the packages.
   `pip install -r .\requirements.txt`

## Week 1: Getting Started

- Installed the necessary software tools.
  - Python
  - VS Code (optional)
  - SQL Server 2022 (Developer)
    - Visual Studio
    - SQL Server Data Tools (SSDT) for Visual Studio
    - PostgreSQL
    - PowerBI Desktop
  - Git

## Week 2: Version Control and Virtual Environment Essentials for Data Professionals

- Used git commands, and created a local repository with virtual environment and learned how to add requirements.txt file that contains the packages needed for reproducibility.

  Commonly used Git commands:

  - git init . #dot for current directory
  - git add . #dot for all changes
  - git commit -m "This is my commit message."
  - git rm your_file_name.ext #used to remove files
  - git push
  - git pull

- Connected the device to a GitHub account and pushed changes to GitHub repository.

## Week 3: Extracting Data from Web to FTP using Python

- Set up WSL.
- Installed vsftpd (FTP server for Unix-like systems) and adjusted its configuration.
- Set up a Python development environment.
- Activated and deactivated the Python development environment.
- Connected to an FTP server and established a secure connection.
- Created a pipeline for data extraction and upload.
- Read CSV data from the web and used config.json file to optimize the process of data extraction
- Uploaded the CSV file to the FTP server, then deleted the file from the local filesystem.
- Wrote a script for manual or scheduled execution of the task.

## Week 4: Loading CSV files from FTP to PostgreSQL using SSIS
