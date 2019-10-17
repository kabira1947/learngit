'''create a sample data base
    create a database "Name"
    use 'Name'
    Create table customers(name VARCHAR(30),age INT(4),email Varchar(30))
    exit
'''


import mysql.connector
from tkinter import *

#WINDOW
window = Tk()

#FRAME

frame= Frame(window)
frame.pack(side=LEFT, padx=20)


#VARIABLE

var1 = StringVar()
cname= StringVar()
var2 =StringVar()
age= int()
var3 =StringVar()
email= StringVar()

#MYSQL CONNECT
#mydb= mysql.connector.connect(host="localhost",user='admin',passwd="pwd",database="MYSQL Python",auth_plugin="mysql_native_password")
#cursor=mydb.cursor()

#Command Function
def addcustomer():
    cname=entry.get()
    age=entry1.get()
    email=entry2.get()
    sql= "INSERT INTO Customer VALUES(%s,%s,%s)"
    #cursor.execute(sql,(cname,age,email))
    #mydb.commit()
    print("Customer Added")
    print(cname)
    print(age)
    print(email)
    return True

#DESIGN

#LEBEL
lebel1= Label(frame,textvar=var1)
var1.set("Customer name")
lebel1.grid(row=0,column=1)

lebel2= Label(frame,textvar=var2)
var2.set("Customer Age")
lebel2.grid(row=1,column=1)

lebel3= Label(frame,textvar=var3)
var3.set("Customer email")
lebel3.grid(row=2,column=1)

#BOXS
entry= Entry(frame,textvar=cname)
cname.set("Enter Name")
entry.grid(row=0,column=2)

entry1= Entry(frame,textvar=age)
cname.set("Enter Age")
entry1.grid(row=1,column=2)

entry2= Entry(frame,textvar=email)
cname.set("Enter Email")
entry2.grid(row=2,column=2)

#BUTTONS
button= Button(frame,text="Add Customer",command=addcustomer)
button.grid(row=3,column=2)

#TITLE AND SIZE
window.title("MYSQL Python")
window.geometry("340x320")
window.resizable(FALSE,FALSE)
window.mainloop()