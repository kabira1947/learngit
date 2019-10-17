from urllib.request import urlopen
import hashlib
Sha1hash= input(" [+] Enter Sha1 Hash value: ")

passlist= str(urlopen("https://raw.githubusercontent.com/paritytech/wordlist/master/res/wordlist.txt").read(),"utf-8")

for password in passlist.split('\n'):
    predicthash= hashlib.sha1(bytes(password,'utf-8')).hexdigest()
    if predicthash == Sha1hash:
        print("[*] The password is : " + str(password))
        quit()
    else:
        print('[*] password guess ' + str(password) + " does not match. Trying the next")
print("password is not in the password list.")