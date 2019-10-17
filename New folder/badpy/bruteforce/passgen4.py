import itertools

wordgen=itertools.product('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=',repeat=2)

for i in wordgen:
    print("".join(i))