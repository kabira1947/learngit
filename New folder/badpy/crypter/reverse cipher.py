msg=input("enter your message: ")

translated=""

i= len(msg)-1

while i>-1:
    translated=translated + msg[i]
    i=i-1
print("the reversed cipher: ",translated)
