with open("phonebook.dat","wb") as f:
    n=int(input('How many entries: '))

    for i in range(n):
        name = input("Enter Name: ")
        phone = input("Enter Mobile number: ")
        name = name.encode()
        phone=phone.encode()
        f.write(name+phone)