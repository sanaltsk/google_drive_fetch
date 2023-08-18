from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

folder_id = '<add folder id>'

file_list = drive.ListFile({'q': "'{0}' in parents and trashed=false".format(folder_id)}).GetList()

for file in file_list:
  print("Downloading " + file['title'])
  downloaded = drive.CreateFile({'id': file['id']})
  downloaded.GetContentFile(file['title'])

print("Done!")
