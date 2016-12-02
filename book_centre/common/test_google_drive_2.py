from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Authenticate the client.
gauth = GoogleAuth()

if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.CommandLineAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()

drive = GoogleDrive(gauth)
