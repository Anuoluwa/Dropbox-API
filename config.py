"""
Config file for the program. All constants should be stored here.
"""
import os
import datetime
from decouple import config

# Retrieves the dropbox API oauth 2 access token saved as an environment variable.
TOKEN = config("TOKEN")

# Sets the log file to the path provided or defaults to the tmp folder.
#You can check the file for logs or errors
LOGFILE = os.environ.get("LOGFILE", "/Users/anuoluwaapiti/Desktop/Dev/logs")

LOCALFILE = '/Users/anuoluwaapiti/Desktop/Dev/ja.py'
BACKUPPATH = '/autodrop' # Keep the forward slash before destination filename