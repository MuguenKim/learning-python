from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import *
from oauth2client import file, client, tools
import os, io, csv
from apiclient.http import MediaIoBaseDownload

# this is an example of bad code. taw n3awdou marra o5ra pour le moment il fonctionne
# le but de ce script est l'import des adresses e-mail de puis google forms
# et de les ecrire dans des fichers CSV


# les permissions sur google(Gmail) API
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
	# permet de telecharger un fichier du drive
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

def downloader(csv_location,file_name):
	# pour telecherger les repenses du google form 
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
    with io.open(csv_location+file_name,'wb') as f:
        fh.seek(0)
        f.write(fh.read())

def import_emails(csv_location):
	# change the data from google forms to csv file divided by class name and 
	# if the student is willing to recive e-mails
	# this is the bad part
	_1GCV = []
	_1GEA = []
	_1LAGQ = []
	_1PREP = []
	_1TC = []
	_2GCV = []
	_2GEA = []
	_2GL = []
	_2LAGQ = []
	_2PREP = []
	_2RT = []
	_3GCV = []
	_3GEA = []
	_3GL = []
	_3LAGQ = []
	_3LF = []
	_3RT = []
	
	classes = ["1GCV","1GEA","1LAGQ","1PREP","1TC","2GCV","2GEA","2GL","2LAGQ","2PREP","2RT","3GCV","3GEA","3GL","3LAGQ","3LF","3RT"]
	_classes = [_1GCV,_1GEA,_1LAGQ,_1PREP,_1TC,_2GCV,_2GEA,_2GL,_2LAGQ,_2PREP,_2RT,_3GCV,_3GEA,_3GL,_3LAGQ,_3LF,_3RT]

	with open(csv_location+"google_forms.csv",'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		
		for line in csv_reader:
			if line['Auth'] == 'Yes':
				if line['Classe'] == '1GCV':
					_1GCV.append(line['Email'])
	
				elif line['Classe'] == '1GEA':
					_1GEA.append(line['Email'])
	
				elif line['Classe'] == '1LAGQ':
					_1LAGQ.append(line['Email'])
	
				elif line['Classe'] == '1PREP':
					_1PREP.append(line['Email'])
	
				elif line['Classe'] == '1TC':
					print("hello")
					_1TC.append(line['Email'])
					
	
				elif line['Classe'] == '2GCV':
					_2GCV.append(line['Email'])
					
				elif line['Classe'] == '2GEA':
					_2GEA.append(line['Email'])
					
				elif line['Classe'] == '2GL':
					_2GL.append(line['Email'])
					
				elif line['Classe'] == '2LAGQ':
					_2LAGQ.append(line['Email'])
					
				elif line['Classe'] == '2PREP':
					_2PREP.append(line['Email'])
					
				elif line['Classe'] == '2RT':
					_2RT.append(line['Email'])
					
				elif line['Classe'] == '3GCV':
					_3GCV.append(line['Email'])
					
				elif line['Classe'] == '3GEA':
					_3GEA.append(line['Email'])
					
				elif line['Classe'] == '3GL':
					_3GL.append(line['Email'])
					
				elif line['Classe'] == '3LAGQ':
					_3LAGQ.append(line['Email'])
					
				elif line['Classe'] == '3LF':
					_3LF.append(line['Email'])
					
				elif line['Classe'] == '3RT':
					_3RT.append(line['Email'])
		j=0			
		for unit in classes:		
			with open(csv_location+unit+".csv",'w') as new_file:
				csv_writer = csv.writer(new_file)
				csv_writer.writerow(_classes[j])
			j+=1
		print("emails import: done!")

def Forms_to_csv(csv_location,file_name):

	#authorization to access google drive Api
	#auth()
	#download the google forms in CSV fomat
	downloader(csv_location,file_name)
	#select data from google forms and separate emails by classes
	import_emails(csv_location)

def check_if_new_emails(csv_location, old_csv_name, new_csv_name):
	downloader(csv_location,new_csv_name)
	old = open(csv_location+old_csv_name, 'r+')
	new = open(csv_location+new_csv_name, 'r')
	old_reader = csv.reader(old)
	new_reader = csv.reader(new)
	old_file = ""
	new_file = ""
	for line in old_reader:
		old_file = old_file + str(line) + '\n'
	old.close()
	for line in new_reader:
		new_file = new_file + str(line) + '\n'
	new.close()
	if old_file != new_file:
			os.remove(csv_location+new_csv_name)
			Forms_to_csv(csv_location,old_csv_name)
			os.remove(csv_location+new_csv_name)
			return True

	else:
		os.remove(csv_location+new_csv_name)
		return False

