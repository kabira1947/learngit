with open ('hello.txt','w+') as f:
    f.write('THAT BOOK BELONGS TO ME')
    print("\n")
    f.write('THAT BOOK BELONGS TO HIM')
    for line in f:
        print(line)

