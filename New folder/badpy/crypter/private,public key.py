# Encryption is done with a public key, while signing is done with a secret key:

from nacl.public import PrivateKey, PublicKey, Box
source = PrivateKey.generate()
with open("target.pubkey", "rb") as fpin:
    target_public_key = PublicKey(fpin.read())
enc_box = Box(source, target_public_key)
result = enc_box.encrypt(b"x marks the spot")
print(result)
b'\xe2\x1c0\xa4'



# Decryption reverses the roles: it needs the private key for decryption and the public key to verify the signature:

from nacl.public import PrivateKey, PublicKey, Box
with open("source.pubkey", "rb") as fpin:
    source_public_key = PublicKey(fpin.read())
with open("target.private_key", "rb") as fpin:
     target = PrivateKey(fpin.read())
dec_box = Box(target, source_public_key)
dec_box.decrypt(result)
b'x marks the spot'