import pandas as pd
import matplotlib.pyplot as plt
import camelot
import time
import sys
import os
import re
import PyPDF2
from cfonts import render, say
os.system("title " + "RAGG(Result Analaysis and Graph Generator) - By Mohammed Zahid Wadiwale")
os.system("mode 160,40")
def name():
	print(render('RAGG', colors=['red', 'yellow'], align='center', size=(160,20)))
	print(render('By Mohammed Zahid', colors=['red', 'yellow'], align='center', size=(160,1)))
def clear():
	os.system('cls')
	name()
def option(question):
	answer = input(question + "(1/2): ").lower().strip()
	while not(answer == "1" or answer == "2"):
		clear()
		answer = input(question + "please enter valid options i.e(1/2):").lower().strip()
	if answer[0] == "1":
		return True
	else:
		return False
name()
options=option(">>>Choose what file format is to be processed!\n1.)Enter 1 for Text PDF file(Not PDF files with Tables)\n2.)Enter 2 for CSV, Excel Formats i.e(XLS,XLSX,XLSM), PDF files containting tables\n>>>Enter Option ")
clear()
if options==False:
	file=input("Enter File Name/Address:")
	print("\n")
	if file.lower().endswith('.pdf'):
		a=camelot.read_pdf(file,flavor='stream', pages = "1-end")
		print(a[0].df)
		time.sleep(1)
		try:
			df = pd.DataFrame(a[0].df)
		except Exception as e:
			print("Make sure the pdf contains proper row and columns format\n"+str(e))
			time.sleep(8)
			sys.exit()
	elif file.lower().endswith('.csv'):
		df = pd.DataFrame(pd.read_csv(file))
	elif file.lower().endswith(('.xlsx','.xlsm')):
		df = pd.DataFrame(pd.read_excel(file,engine='openpyxl'))
	elif file.lower().endswith('.xls'):
		df = pd.DataFrame(pd.read_excel(file,engine='xlrd'))
	else:
		print("The Format is not supported.")
		time.sleep(8)
		sys.exit()
	new_header = df.iloc[0]
	df = df[1:]
	df.columns = new_header
	print("Following are column names:\n"+str(df.columns))
	try:
		cols=input("Enter Column Name(Case Sensitive):")
		asf=df[cols]
	except:
		print("Error No Such Column Exists")
		time.sleep(8)
		sys.exit()
	dsf=asf.value_counts()
	dsfv=dsf.to_dict()
	print(dsfv)
	plt.bar(range(len(dsfv)), list(dsfv.values()), align='center')
	plt.xticks(range(len(dsfv)), list(dsfv.keys()))
	plt.show()
	time.sleep(15)
	sys.exit()
elif options==True:
	textsfile=[]
	sword=""
	print(":::>>>The current keyword is :\""+sword+"\"\n:::>>>To Change it edit keyword inside keyword.txt\n")
	pdf=input("Enter PDF Name(Dont add .pdf ahead):")
	with open(pdf+".pdf", mode='rb') as f:
		reader = PyPDF2.PdfFileReader(f)
		for page in reader.pages:
			textsfile.append(page.extractText())
	with open(pdf+".txt", 'w') as f:
		for item in textsfile:
			f.write("%s\n" % item)
	ff = open(pdf+".txt")
	txt=str(ff.read())
	with open("keyword.txt", mode='r') as f:
		sword=f.read()
	sword=sword[1:-1]
	print(sword)
	a=[m.start() for m in re.finditer(sword, txt)]
	if not a:
		print(">>>Error: The Keyword \""+str(sword)+"\" is not found")
		time.sleep(8)
		sys.exit()
	K = int(len(sword))
	res = [x + K for x in a]
	d=[]
	for i in res:
		try:
			d.append(float(txt[i:i+4]))
		except ValueError:
			d.append(float(0.00))
	print(d)
	print("\nNo of failed students:"+str(d.count(0.00)))
	print("\nNo of passed Students:"+str(len(d)-d.count(0.00)))
	print("\nTotal Students:"+str(len(d)))
	print("\nAverage GPA:"+str(sum(d)/len(d)))
	a5,a55,a6,a65,a7,a75,a8,a85,a9,a95,a10=1,1,1,1,1,1,1,1,1,1,1
	for i in d:
		if i>0.0 and i<5.5:
			a5=a5+1
		elif i>=5.5 and i<6.0:
			a55=a55+1
		elif i>=6.0 and i<6.5:
			a6=a6+1
		elif i>=6.5 and i<7.0:
			a65=a65+1
		elif i>=7.0 and i<7.5:
			a7=a7+1
		elif i>=7.5 and i<8.0:
			a75=a75+1
		elif i>=8.0 and i<8.5:
			a8=a8+1
		elif i>=8.5 and i<9.0:
			a85=a85+1
		elif i>=9.0 and i<9.5:
			a9=a9+1
		elif i>=9.5 and i<=10.0:
			a95=a95+1
	print("\nNo of students getting less than 5.5 GPA:"+str(a5-1))
	print("\nNo of students getting in between 5.5-6 GPA:"+str(a55-1))
	print("\nNo of students getting in between 6-6.5 GPA:"+str(a6-1))
	print("\nNo of students getting in between 6.5-7 GPA:"+str(a65-1))
	print("\nNo of students getting in between 7-7.5 GPA:"+str(a7-1))
	print("\nNo of students getting in between 7.5-8 GPA:"+str(a75-1))
	print("\nNo of students getting in between 8-8.5 GPA:"+str(a8-1))
	print("\nNo of students getting in between 8.5-9 GPA:"+str(a85-1))
	print("\nNo of students getting in between 9-9.5 GPA:"+str(a9-1))
	print("\nNo of students getting in between 9.5-10 GPA:"+str(a95-1))
	thegame={"failed":int(d.count(0.00)),"<5.5 GPA":int(a5-1),"5.5-6 GPA":int(a55-1),"6-6.5 GPA":int(a6-1),"6.5-7 GPA":int(a65-1),"7-7.5 GPA":int(a7-1),"7.5-8 GPA":int(a75-1),"8-8.5 GPA":int(a8-1),"8.5-9 GPA":int(a85-1),"9-9.5 GPA":int(a9-1),"9.5-10 GPA":int(a95-1)}
	plt.bar(range(len(thegame)), list(thegame.values()), align='center')
	plt.xticks(range(len(thegame)), list(thegame.keys()))
	plt.show()
	time.sleep(15)
	sys.exit()
