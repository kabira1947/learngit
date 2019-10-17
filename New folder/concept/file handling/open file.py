from tkinter import filedialog
from tkinter import *
root=Tk()
root.title("File Dialog")

def open_file():
    filename=filedialog.askopenfilename(parent=root,title="Select a File",filetypes=(("Python files","*.py"),("All files","*.*")))
    if filename != None:
        f = open(filename, 'r')
        contents = f.read()
        # create a text box and add it to root windows
        t = Text(root, width=80, height=20, wrap=WORD)
        t.pack()
        # insert thr file contents in the text box
        t.insert(1.0, contents)
        # close the file
        f.close()

def save_file():
    filename=filedialog.asksaveasfilename(parent=root,title="Select a File",filetypes=(("Python files","*.py"),("All files","*.*")))
    if filename != None:
        f = open(filename,'w')
        # insert thr file contents in the text box
        t = Text(root, width=80, height=20, wrap=WORD)
        contents=str(t.get(1.0,END))
        f.write(contents)
        # close the file
        f.close()
b1= Button(root,text="Open file",width=15,height=2,command=save_file)
b1.place(x=100, y=200)
b2= Button(root,text="Save file",width=15,height=2,command=open_file)
b2.place(x=400, y=200)
root.geometry('600x400')
root.mainloop()
