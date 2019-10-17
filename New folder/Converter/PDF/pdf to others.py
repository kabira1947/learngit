import PyPDF2
name = input("enter the file name: ")
filename = ("{}.pdf".format(name))
pdffile = open(filename,"rb")
pdfreader = PyPDF2.PdfFileReader(pdffile)
x = pdfreader.numPages
for pages in range(x):
    page = pdfreader.getPage(pages)
    text = page.extractText()
    print(pages,text)

'''print(x)
print(page)
'''
'''
file1=open(r"{}.txt".format(name),"a")
file1.writelines(text)
file1.close()


file2=open(r"{}.excel".format(name),"a")
file2.writelines(text)
file2.close()

file3=open(r"{}.docx".format(name),"a")
file3.writelines(text)
file3.close()

file4=open(r"{}.json".format(name),"a")
file4.writelines(text)
file4.close()
'''