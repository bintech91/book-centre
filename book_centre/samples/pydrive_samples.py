from pydrive.auth import  GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello12333sssss.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello Worlsssd!') # Set content of the file from given string.
file1.Upload()

file2 = drive.CreateFile({'title': 'Hellos123ssss.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file2.SetContentString('Hello W123123orlsssd!') # Set content of the file from given string.
file2.Upload()