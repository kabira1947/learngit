import PyPDF2
pdffileobj=open('Prabhhu Kalyan Samal CV August 2019.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

file1=open(r"Prabhhu Kalyan Samal CV August 2019.txt","a")
file1.writelines(text)
file1.close()