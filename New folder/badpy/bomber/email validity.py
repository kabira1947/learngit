import re
email=input("enter the email:- ")
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):

    if (re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")
check(email)

