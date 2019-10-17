str= input("Enter the number of characters in String : ")

i=0

# number of characters
for s in str:
   # print(str[i],end=' ')
    i+=1
print('enter the number of characters =',i,end='\n')

# number of characters without space
line= str.split(" ")
total=0
for x in line:
    total += len(x)
print("total character without space : ",total)


'''
# numbers of a letter
number = str.count(input("type the letter: "))
print(number)
'''

