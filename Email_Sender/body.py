from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from forms_to_csv import Forms_to_csv, check_if_new_emails
import csv, time, os, re, datetime, smtplib

#Variable a changer
email_user = 'essat.gabes.uni@gmail.com'
forms_csv_name = "google_forms.csv"
csv_location="E:/python script/learning-python/Email_Sender/CSV/"
files_location="E:/python script/learning-python/Email_Sender/Files/"
email_password="Password-01"
#email_password = input("Enter le mot de passe de l'adresse email: \n"+email_user+"\n")



def makecsv(files_location,csv_location):
	#make CSV file for all the files
	f=open(csv_location+"files.csv", 'w')
	writer = csv.writer(f)
	writer.writerow(['file_name', 'time'])
	for path,dirs,files in os.walk(files_location):
		for filename in files:
			time = os.path.getctime(files_location+filename)
			stamp = os.stat(files_location+filename).st_mtime
			#print(stamp)
			if filename != 'files.csv': 
				writer.writerow([filename, stamp])

def check():
	#check if new file
	#return list of new files
	#return bool False if no new
	new_files_path=[]
	with open(csv_location+"files.csv",'r+') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		csv_writer = csv.writer(csv_file)
		for line in csv_reader:
			file_path = files_location+line['file_name']
			new_time = str(os.path.getctime(file_path))
			new_stamp = str(os.stat(file_path).st_mtime)
			#print(line['time'] + "\t" + new_stamp)
			if line['time'] != new_stamp:
				new_files_path.append(file_path)
			

	if new_files_path != []:
		return new_files_path
	else :
		return False
#print(check())
#new_files_path=['C:/Users/mugue/OneDrive/python script/email sender/Files/1GCV.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/1GEA.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/1LAGQ.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/1PREP.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/1TC.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/2GCV.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/2GEA.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/2GL.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/2LAGQ.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/2PREP.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/2RT.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/3GCV.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/3GEA.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/3GL.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/3LAGQ.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/3LF.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/3RT.pdf', 'C:/Users/mugue/OneDrive/python script/email sender/Files/files.csv']

def get_class(new_files_path):
	#argument is a list
	#get class name from files path
	#return list
	class_names = []
	pattern = re.compile(r'([1-3])\w+')
	for i in new_files_path:
		name = pattern.search(i)
		class_names.append(name.group(0))
	return class_names
#print(get_class(new_files_path))
#class_name=['1GCV', '1GEA', '1LAGQ', '1PREP', '1TC', '2GCV', '2GEA', '2GL', '2LAGQ', '2PREP', '2RT', '3GCV', '3GEA', '3GL', '3LAGQ', '3LF', '3RT']

def get_address(class_name):
	#argument is a string
	#return a list with all the email adresses of the class
	class_csv_location = csv_location+class_name+".csv"
	with open(class_csv_location,'r') as csv_file:
		emails = []
		csv_reader = csv.reader(csv_file)
		for line in csv_reader:
			emails.append(line)
	return emails
#print(get_address("1GCV"))

#email_send =['muguen.kim@gmail.com', 'Walid.cherif.tunisia@gmail.com', 'muguen.kim1@gmail.com']
#file_name ="1GCV.pdf"

def send(email_send, file_name,subject):
	#mots de passe de l'email

	#Creation du message
	now = datetime.datetime.now()
	now = now.strftime('%Hh, %d, %b %Y')
	filename = file_name

	msg = MIMEMultipart()
	msg['From'] = email_user
	msg['To'] = ", ".join(email_send)
	msg['Subject'] = subject
	body = "changement de l'emploi du temps à " +str(now)
	msg.attach(MIMEText(body,'plain'))
	attachement = open((files_location+file_name),'rb')

	part = MIMEBase('application','octet-stream')
	part.set_payload(attachement.read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachement; filename= "+filename)
	
	msg.attach(part)
	#convertir l'object en text
	text=msg.as_string()
	
	#Information et login au serveur SMTP
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.set_debuglevel(1)
	server.starttls()
	server.login(email_user,email_password)
	
	#Envoi du message
	server.sendmail(email_user,email_send,text)
	server.quit()
#send(email_send,file_name)


if not os.path.isfile(csv_location+"files.csv"):
	print("no file here")
	makecsv(files_location, csv_location)

Forms_to_csv(csv_location,forms_csv_name)

while True:
	check_if_new_emails(csv_location, forms_csv_name, "new_google_forms.csv")
	new_files_path = check()
	if new_files_path != False:
		print("il existe "+str(len(new_files_path))+" nouveau(x) element(s)")
		class_names = get_class(new_files_path)
		for element in class_names:
			subject = 'Emploi du temps pour '+element
			print(subject)
			emails = get_address(element)
			file_name =element+".pdf"
			print(file_name)
			send(emails,file_name,subject)
	
		
	else:
		print('No new files. Another check will be done in one hour.')
	makecsv(files_location,csv_location)
	time.sleep(3600)