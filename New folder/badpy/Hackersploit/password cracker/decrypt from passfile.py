import hashlib
MD5hash= input(" [+] Enter MD5 Hash value: ")

passlist= open('wordlist.txt','r')


for password in passlist:
    predicthash= hashlib.md5(bytes(password.strip(),'utf-8')).hexdigest()
    if predicthash == MD5hash:
        print("[*] The password is : " + str(password))
        quit()
    else:
        print('[*] password guess ' + str(password) + " does not match. Trying the next---")

print("password is not in the password list.")