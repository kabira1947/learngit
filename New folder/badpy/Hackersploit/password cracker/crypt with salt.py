import crypt


sentence= input("the the line you want to crypt: ")
Salting= input("enter the salting value you want to add: ")

cryptline= crypt.crypt(sentence,salt='Salting')

print(cryptline)
