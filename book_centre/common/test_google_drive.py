from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import argparse

PARENT_ID = "LONG_FOLDER_ID_STRING"

# Parse the passed arguments
parser = argparse.ArgumentParser()
parser.add_argument("files", help="List files to be uploaded.", nargs="+")

# Define the credentials folder
home_dir = os.path.expanduser("~")
credential_dir = os.path.join(home_dir, ".credentials")
if not os.path.exists(credential_dir):
    os.makedirs(credential_dir)
credential_path = os.path.join(credential_dir, "google_auth.json")

# Start authentication
gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile(credential_path)
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.CommandLineAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile(credential_path)

drive = GoogleDrive(gauth)

# Upload the files
for f in parser.parse_args().files:
    new_file = drive.CreateFile({"parents": [{"id": PARENT_ID}], \
                                 "mimeType": "text/plain"})
    new_file.SetContentFile(f)
    new_file.Upload()
