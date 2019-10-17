from tkinter import *
import tkinter.messagebox
root =Tk()
root.geometry('500x500')
root.title('Tikinter')
root.configure(background="green")

#input format
textin= StringVar()

#dictionary

exlist={'Abhishek':'Information Tech','Sam':'Mechanical','Jack':'Computer','Erik':'Electronics','john':'Robotics',
        'Mayur':'Information Tech','Akshay':'Robotics','Bhavesh':'Computer','Sameer':'Electronics','Sagar':'Robotics'}

def clk():
    pass
def help():
    pass
def save():
    pass
def saveas():
    pass
def ex():
    pass
def exit():
    pass
def Print():
    pass
def importfile():
    pass
def clear():
    pass
def about():
    pass
def version():
    pass
#menu

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label='Help', command=help())
submenu.add_command(label='Import', command=importfile())
submenu.add_command(label='Save', command=save())
submenu.add_command(label='Save as', command=saveas())
submenu.add_command(label='Print',command=Print())
submenu.add_command(label='Exit', command=ex())

submenu1 = Menu(menu)
menu.add_cascade(label= 'About us', menu=submenu1)

submenu2 = Menu(menu)
menu.add_cascade(label='version', command= version)

stubox = Label(root,text='Name :',font=('none 20 bold'),background=('blue'))
stubox.grid(row=0, column=1, sticky= W)

stubox1= Entry(root,width=20,  font=('none 20 bold'))
stubox1.grid(row=0,column=3,sticky= W)

root.mainloop()