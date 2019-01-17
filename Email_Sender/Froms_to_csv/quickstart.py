from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import *
from oauth2client import file, client, tools
import os, io
from apiclient.http import MediaIoBaseDownload

# le but de ce script est l'import des emails de puis google forms
SCOPES = 'https://www.googleapis.com/auth/drive.readonly'



def auth():
    #code donné par google
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    drive_service = build('drive', 'v3', http=creds.authorize(Http()))
    

def listFiles(size):
    #code donné par google
    # Call the Drive v3 API
    results = drive_service.files().list(
        pageSize=size, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

def downloadFile(file_id, file_path):
    request = drive_service.files().export_media(fileId=file_id,
                                             mimeType='text/csv')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
    with io.open(file_path,'wb') as f:
        fh.seek(0)
        f.write(fh.read())

def downloader():
    file_path = "E:/python script/email sender/CSV/google_forms.csv"
    file_id = '1gFwGMC0_0uzPK62fLsjumVGZXeSTmw1eyE69gtgrLzQ'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    drive_service = build('drive', 'v3', http=creds.authorize(Http()))
    request = drive_service.files().export_media(fileId=file_id,
                                             mimeType='text/csv')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
    with io.open(file_path,'wb') as f:
        fh.seek(0)
        f.write(fh.read())
