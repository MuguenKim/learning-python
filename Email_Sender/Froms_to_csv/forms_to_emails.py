import csv

#this an example of bad code. taw n3awdou marra o5ra pour le moment il fonctionne

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
def import_emails():
	with open('E:/python script/email sender/CSV/google_forms.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		
		for line in csv_reader:
			if line['Auth'] == 'Yes':
				#need to optimise code here:
				if line['Classe'] == '1GCV':
					_1GCV.append(line['Email'])
	
				elif line['Classe'] == '1GEA':
					_1GEA.append(line['Email'])
	
				elif line['Classe'] == '1LAGQ':
					_1LAGQ.append(line['Email'])
	
				elif line['Classe'] == '1PREP':
					_1PREP.append(line['Email'])
	
				elif line['Classe'] == '1TC':
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
			with open('E:/python script/email sender/CSV/'+unit+".csv",'w') as new_file:
				csv_writer = csv.writer(new_file)
				csv_writer.writerow(_classes[j])
			j+=1
		print("emails import: done!")
import_emails()
	