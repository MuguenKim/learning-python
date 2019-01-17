from body import *
import time 

#Variable a changer
csv_location="E:/python script/email sender/CSV/"
files_location="E:/python script/email sender/Files/"

while True:
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
		print('No new files. Another check will be done in 10min.')
	makecsv(files_location,csv_location)
	time.sleep(3600)