import sys
import dropbox
import logging
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import config

# Access token
TOKEN = config.TOKEN

LOCALFILE = config.LOCALFILE
BACKUPPATH = config.BACKUPPATH

# Set up logging.
logging.basicConfig(filename=config.LOGFILE, level=logging.INFO)

# Uploads contents of LOCALFILE to Dropbox
def backup():
    with open(LOCALFILE, 'rb') as f:
        # WriteMode=overwrite ensures that the settings in the file
        # are changed on upload
        logging.info("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # Checks for the specific error where a user doesn't have enough Dropbox space size to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                logging.info(err.user_message_text)
                sys.exit()
            else:
                print(err)
                logging.info(err)
                sys.exit()


# Few functions to check file details
def checkFileDetails():
    logging.info("Checking file details")
    print("Checking file details")

    for entry in dbx.files_list_folder('').entries:
        logging.info(entry.name)
        print("File list is : ")
        print(entry.name)


# Run this script independently
if __name__ == '__main__':
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Please add your access token, looks like you didn't add your access token.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    logging.info("Creating a Dropbox object...")
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the DropBox app console on the web.")

    try:
        checkFileDetails()
    except Error as err:
        sys.exit("Error while checking file details")
    logging.info("Creating backup...")
    print("Creating backup...")
    # Create a backup of the current settings file
    backup()

    logging.info("Process Completed!")
    print("Process Completed!")