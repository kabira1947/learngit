srt= input("enter the string : ")
sub=input("enter the sub string: ")
n= input("enter the position to put the substring: ")

n-=1

l1=len(srt)
l2=len(sub)

srt1= []

for i in range (n):
    srt1.append(srt[i])
