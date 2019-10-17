import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "EMAIL address of the sender"
toaddr = "EMAIL address of the receiver"

msg = MIMEMultipart()  # instance of MIMEMultipart

msg['From'] = fromaddr  # storing the senders email address

msg['To'] = toaddr  # storing the receivers email address

msg['Subject'] = "Subject of the Mail"  # storing the subject

body = "Body_of_the_mail"  # string to store the body of the mail

msg.attach(MIMEText(body, 'plain'))  # attach the body with the msg instance

filename = "File_name_with_extension"  # open the file to be sent
attachment = open("Path of the file", "rb")

p = MIMEBase('application', 'octet-stream')  # instance of MIMEBase and named as p

p.set_payload((attachment).read())  # To change the payload into encoded form

encoders.encode_base64(p)  # encode into base64

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)  # attach the instance 'p' to instance 'msg'

s = smtplib.SMTP('smtp.gmail.com', 587)  # creates SMTP session

s.starttls()  # start TLS for security

s.login(fromaddr, "Password_of_the_sender")  # Authentication

text = msg.as_string()  # Converts the Multipart msg into a string

s.sendmail(fromaddr, toaddr, text)  # sending the mail

s.quit()  # terminating the session
