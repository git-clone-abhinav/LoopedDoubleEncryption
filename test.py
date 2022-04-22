from Crypto.Cipher import AES
import hashlib, util

password = "hello there".encode()
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = "This is an IV465"

cipher = AES.new(key,mode,IV)
message = util.padmessage("test message")
message = message.encode()
e_message = cipher.encrypt(message)
print(e_message)