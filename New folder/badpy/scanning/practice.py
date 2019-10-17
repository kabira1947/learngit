list1=[55,43,55,23,44,34,43,1,23,23,23]

list=[]

for i in list1:
     if i not in list:
         list.append(i)

print(list)