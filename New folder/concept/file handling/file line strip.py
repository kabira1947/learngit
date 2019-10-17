def strip1():
    f = open("likun.txt", "r")
    str=f.readlines()
    for i in str:
        print(i.strip(), end="\n")
    f.close()
strip1()