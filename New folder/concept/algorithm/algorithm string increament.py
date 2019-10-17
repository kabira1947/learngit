string = str(input("please enter the string = "))
lenght = len(string)
for i in range(lenght):
    for j in range(i+1):
        print(string[i],end="")
    print()

String = str(input("please enter the string = "))
lenght = len(string)
for i in range(lenght):
    for j in range(i+1):
        print(string[j],end="")
    print()