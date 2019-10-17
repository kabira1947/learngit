f= open("likun.txt","r+")
#for i in range(10):
 #    f.write("This is line %d\r\n" % (i+1))

#f.write("hello how r u")
str=f.read()
print(str)
f.close()