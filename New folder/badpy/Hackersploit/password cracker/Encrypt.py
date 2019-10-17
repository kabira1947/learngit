import hashlib

hashvalue = input("* Enter a String: ")

#MD5
hashobj = hashlib.md5()
hashobj.update(hashvalue.encode())
print(hashobj.hexdigest())

#SHA1
hashobj1= hashlib.sha1()
hashobj1.update(hashvalue.encode())
print(hashobj1.hexdigest())

#SHA224
hashobj2= hashlib.sha224()
hashobj2.update(hashvalue.encode())
print(hashobj2.hexdigest())

#SHA512
hashobj3= hashlib.sha512()
hashobj3.update(hashvalue.encode())
print(hashobj3.hexdigest())

#Blake2b
hashobj4= hashlib.blake2b()
hashobj4.update(hashvalue.encode())
print(hashobj4.hexdigest())

