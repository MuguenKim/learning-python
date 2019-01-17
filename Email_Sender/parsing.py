import csv

with open('E:/python script/email sender/CSV/', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for line in csv_reader:
		print(line['email'])

#with open('names.csv', 'r') as csv_file:
#	csv_reader = csv.DictReader(csv_file)
#
#	with open('new_manes.csv', 'w') as new_file:
#			fieldnames = ['first_name', 'last_name','county', 'zip', 'phone1', 'company_name', 'address', 'state', 'phone', 'city', 'email']
#
#			csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#			csv_writer.writeheader()
#
#			for line in csv_reader:
#				csv_writer.writerow(line)
#
