A= input("Enter file :  ")

if len(A)<1 : A= 'log.txt'

file1= open(A,'r')
#file= file1.read().lower()  (only lower cases)
file= file1.read()
di= dict()
for line in file:
    line= line.rstrip()
    words=line.split()
    for word in words:
        di[word] = di.get(word,0) + 1

largest= -1
the_word= None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest=v
        the_word=k

print("the largest is:",the_word,largest,"times used")
