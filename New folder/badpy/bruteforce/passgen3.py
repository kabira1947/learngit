import string
from random import *

letters= string.ascii_letters +string.digits+string.ascii_uppercase+string.ascii_lowercase
#while True:
password= "".join(choice(letters)for x in range(randint(4,8)))
print(password)
    