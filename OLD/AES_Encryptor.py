from Crypto.Cipher import AES
import hashlib
import util


# generating a random key of 1000 letters
password = util.keygen(1000)
with open('password.txt', 'w') as f:
    f.write(password)
password = password.encode() #converting it to bytes

# hashing it with SHA256
key  = hashlib.sha256(password).digest()
with open('AES_Hashed_key.txt', 'w') as f:
    f.write(key.hex())

mode = AES.MODE_CBC # Cypher Blockchain Mode
IV = 'This is an IV465' # Initialisation Vector should be of 16 bytes (a randomised string)

cipher = AES.new(key,mode,IV)

message = util.padmessage('This is a secret message')

encrypted_message = cipher.encrypt(message)

print(encrypted_message)