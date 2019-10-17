from tkinter import *
import mysql.connector
from tkinter import ttk
#WINDOWS

window=Tk()
frame= Frame(window)
frame.pack(side=LEFT,padx=20)

table= ttk.Treeview(frame,columns=(1,2,3),show='headings',height='5')
table.pack()

table.heading(1,text="Name")
table.heading(2,text="Age")
table.heading(3,text='email')

#DB
mydb=mysql.connector.connect()
cursor=mydb.cursor()
sql="SELECT * FROM customers"
cursor.execute(sql)
rows=cursor.fetchall()
total= cursor.rowcount


for i in rows:
    table.insert('','end',values=i)

#Title

window.title('mysql table')
window.geometry('350x350')
window.resizable(False,False)
window.mainloop()

