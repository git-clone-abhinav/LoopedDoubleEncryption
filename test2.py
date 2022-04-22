import base32hex
import hashlib
from Crypto.Cipher import DES
with open("keyfile.txt", 'r') as f:
    key = f.read()
    print(key)
key = key.encode()
iv = b'constant'
crypter = DES.new(key, DES.MODE_CBC, iv)

plain_text= b"I see you"

print("The plain text is : ",plain_text)
plain_text += b'\x00' * (8 - len(plain_text) % 8) # bytes
ciphertext = crypter.encrypt(plain_text)
encode_string= base32hex.b32encode(ciphertext)
print("The encoded string is : ",encode_string)

crypto = DES.new(key, DES.MODE_CBC, iv)

encrypted_string=base32hex.b32decode(encode_string)
decrypted_string = crypto.decrypt(encrypted_string)
print("The decrypted string is : ",decrypted_string)