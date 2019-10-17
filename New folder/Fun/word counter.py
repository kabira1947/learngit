A= input("Enter file :  ")

if len(A)<1 : A= 'log.txt'

file= open(A,'r')
di= dict()
for line in file:
    line= line.rstrip()
    words=line.split()
    for word in words:
        di[word] = di.get(word,0) + 1

largest= -1
smallest= 99
the_word= None
less_used= None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest=v
        the_word=k
for k,v in  di.items():
    if v<smallest:
        smallest=v
        less_used=k

print("the largest is:",the_word,largest,"times used")

print("the lowest is: ",less_used,smallest,"times used")
