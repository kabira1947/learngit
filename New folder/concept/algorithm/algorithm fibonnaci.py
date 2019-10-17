fib= int(input("please enter a number = "))
first=0
second=1
for i in range(fib):
    print(first)
    temp=first
    first=second
    second=temp+second
print(second,"\n")
