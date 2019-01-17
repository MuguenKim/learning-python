import os
import csv

csv_location="E:/python script/email sender/CSV/"
files_location="E:/python script/email sender/Files/"
def makecsv(files_location,csv_location):
	#make CSV file for all the files
	f=open(csv_location+"files.csv", 'w')
	writer = csv.writer(f)
	writer.writerow(['file_name', 'time'])
	for path,dirs,files in os.walk(files_location):
		for filename in files:
			time = os.path.getctime(files_location+filename)
			stamp = os.stat(files_location+filename).st_mtime
			print(stamp)
			if filename != 'files.csv': 
				writer.writerow([filename, stamp])
makecsv(files_location,csv_location)