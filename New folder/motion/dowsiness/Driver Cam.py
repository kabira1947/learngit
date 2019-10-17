import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('600x670')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Driver Cam')
frame.config(background='light blue')
label = Label(frame, text="Camera Jobs",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)



def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Prabhu \n 2. Priyam \n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v2.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()
def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         eyes = eye_cascade.detectMultiScale(roi_gray)


         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()
def face_simile():
    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    def detect(gray, frame):
        font = cv2.FONT_HERSHEY_COMPLEX
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
                cv2.addText(frame, 'Face', (x + w, y + h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
        return frame

    while True:
        # Captures video_capture frame by frame
        _, frame = video_capture.read()

        # To capture image in monochrome
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # calls the detect() function
        canvas = detect(gray, frame)

        # Displays the result on camera feed
        cv2.imshow('Video', canvas)

        # The control breaks once q key is pressed
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    # Release the capture once all the processing is done.
    video_capture.release()
    cv2.destroyAllWindows()
   
but1=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 8 bold'))
but1.place(x=5,y=80)

but2=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 8 bold'))
but2.place(x=5,y=140)

but3=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 8 bold'))
but3.place(x=5,y=200)

but4=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 8 bold'))
but4.place(x=5,y=260)

but5=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Eye Blink & Record With Sound',font=('helvetica 8 bold'))
but5.place(x=5,y=320)

but6=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Night Vison',font=('helvetica 8 bold'))
but6.place(x=5,y=380)

but8=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Image face Detector',font=('helvetica 8 bold'))
but8.place(x=5,y=440)

but9=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Car Detector',font=('helvetica 8 bold'))
but9.place(x=5,y=500)

but10=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Car Speed Detector',font=('helvetica 8 bold'))
but10.place(x=300,y=80)

but11=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Lane Detector',font=('helvetica 8 bold'))
but11.place(x=300,y=140)

but12=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Color Detector',font=('helvetica 8 bold'))
but12.place(x=300,y=200)

but13=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Third Umpire',font=('helvetica 8 bold'))
but13.place(x=300,y=260)

but14=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Suduko Solver',font=('helvetica 8 bold'))
but14.place(x=300,y=320)

but15=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='Speed Detector',font=('helvetica 8 bold'))
but15.place(x=300,y=380)

but16=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=face_simile,text='Face and Smile',font=('helvetica 8 bold'))
but16.place(x=300,y=440)

but17=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='XX',font=('helvetica 8 bold'))
but17.place(x=300,y=500)

#but18=Button(frame,padx=5,pady=5,width=30,bg='white',fg='black',relief=GROOVE,command=blink,text='XXX',font=('helvetica 5 bold'))
#but18.place(x=300,y=540)

but7=Button(frame,padx=5,pady=5,width=7,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but7.place(x=210,y=590)


root.mainloop()

