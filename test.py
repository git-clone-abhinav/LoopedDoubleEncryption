from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad,pad
import util

key = util.keygen(8)

with open('keyfile.txt', 'w') as f:
    f.write(key)
    print(f"Written DES key to file {key}")

key = key.encode()
cypher = DES.new(key, DES.MODE_ECB)

with open("rankers.txt", 'r') as f:
    AES_cypher_text = f.read()
    print(f"Read text form rankers.txt")

AES_cypher_text = AES_cypher_text.encode()
cypher_text = cypher.encrypt(pad(AES_cypher_text, 8))

with open('cypher.txt', 'w') as f:
    f.write(cypher_text.hex())
    print("Written DES Cypher Text to file")


with open("keyfile.txt", 'r') as f:
    key = f.read()
    print(key)
key = key.encode() #converting it to bytes
with open("cypher.txt", "r") as f:
    cyphertext = f.read()
    print(f"Read Cypher Text cypher.txt {cyphertext}")

ciphertext = bytes.fromhex(cyphertext)
cipher = DES.new(key, DES.MODE_CBC)
plaintext = cipher.decrypt(ciphertext)

with open('recovery.txt', 'w') as f:
    f.write(plaintext.hex())
    print(f"Wrote to recovery.txt")

if 1==0:
    import os
    os.remove('keyfile.txt')
    os.remove('cypher.txt')
    os.remove('recovery.txt')
    print("Removed files")