from string import *

rot13trans = bytes.maketrans(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                             b'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
text= input("The line to encrypty: ")

rot13 = text.translate(rot13trans)
print(rot13)
