A= input("Enter file :  ")

if len(A)<1 : A= 'log.txt'

file= open(A,'r').read()
di= dict()
for line in file:
    line= line.rstrip().lower()
    words=line.split()
    for word in words:
        di[word] = di.get(word,0) + 1

tmp=list()
for k,v in di.items():
    newt=(v,k)
    tmp.append(newt)
tmp=sorted(tmp,reverse=True)
for v,k in tmp:
    print(k,v)

