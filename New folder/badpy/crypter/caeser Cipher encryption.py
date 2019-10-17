msg=input("enter the string: ")

shift=int(input("enter the number of shifts: "))

result=""

for i in range(len(msg)):
    char=msg[i]
    if (char.isupper()):
        result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
    else:
        result += chr((ord(char) + shift - 97) % 26 + 97)

print(result)