#uploaded
from win32com.client import Dispatch

file=input("file path : ")
filename=open("word.txt","r")
passlist = filename.readline()
passwords= passlist.split('\n')
filename.close()
applied=0
for password in passlist:
    print("password testing:{}".format(password))
    exucute=Dispatch("Excel.Application")
    try:
        exucute.Workbooks.open(file,False,True,None,password)
        print("password cracked:"+ password)
        break
    except:
        pass

"""
1) excel file import
2) a) word file import
   b) read the pass file
   c) split it to column
   d) place to implement the pass
   e) password found or not

"""

