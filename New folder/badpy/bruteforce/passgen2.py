import string
import random


def generate(num):
    password = ''

    for n in range(num):
        x = random.randint(0, 86)
        password += string.printable[x]

    return password


# generate and print a 16 character random password


print(generate(16))
"""
1) pass value none
2) RANDOM CHARACTERS
3) add pass value from random characters
4) return password as number of character required
"""