from cryptography.fernet import Cipher,Fernet

key= Fernet.generate_key()

frn = Fernet(key)

encryption= frn.encrypt(b"x marks the spot")
print(encryption)

decryption= frn.decrypt(encryption)
print(decryption)