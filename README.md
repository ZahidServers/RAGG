# RAGG
It is a Python Code to Generate graph of students passed and failed no of A grades, B Grades, etc from csv, excel sheets or pdf of marksheets of all students of college provided by university. This code was created by me i.e Mohammed Zahid Wadiwale for my College VSIT
---
Usually Mumbai University have some standard patterns of results which it sends to colleges.
Usually its Excel Sheets(CSV,XLS,XLSX,XLSM,etc) or PDFs in either Table Format like Excel or PDFs in Text Format.
RAGG gives two option one for Excel Formats and PDF containing Tables other is for TEXT PDF.
For files having tables RAGG converts them into Dataframes then gives list of columns and ask user to enter the column they want i.e(REMARKS Column, Grades, CGI, etc).
For PDFs having Text patterns RAGG looks for paticular keyword like " CGI  : " which is default keyword which RAGG looks for can be changed by editing keyword inside inverted commas in keyword.txt
