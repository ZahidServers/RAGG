import pandas as pd
import matplotlib.pyplot as plt
import camelot
import time
import sys
import os
os.system("title " + "RGG(Result Graph Generator) - By Mohammed Zahid Wadiwale")
file=input("Enter File Name/Address:")
print("\n")
if file.lower().endswith('.pdf'):
	a=camelot.read_pdf(file, pages = "1-end")
	a.export('output.csv', f='csv', compress=True)
	time.sleep(1)
	df = pd.DataFrame(pd.read_csv("output.csv"))
elif file.lower().endswith('.csv'):
	df = pd.DataFrame(pd.read_csv(file))
elif file.lower().endswith(('.xlsx','.xlsm')):
	df = pd.DataFrame(pd.read_excel(file,engine='openpyxl'))
elif file.lower().endswith('.xls'):
	df = pd.DataFrame(pd.read_excel(file,engine='xlrd'))
else:
	print("The Format is not supported.")
	time.sleep(6)
	sys.exit()
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header
try:
	cols=input("Enter Column Name(Case Sensitive):")
	asf=df[cols]
except:
	print("Error No Such Column Exists")
	time.sleep(5)
	sys.exit()
dsf=asf.value_counts()
dsfv=dsf.to_dict()
print(dsfv)
plt.bar(range(len(dsfv)), list(dsfv.values()), align='center')
plt.xticks(range(len(dsfv)), list(dsfv.keys()))
plt.show()
if file.lower().endswith('.pdf'):
	os.remove('output.csv')
time.sleep(10)
sys.exit()
