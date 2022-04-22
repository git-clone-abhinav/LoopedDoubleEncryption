def decrypt(keyfile,filename):
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import unpad
    import logger

    with open(keyfile, 'r') as f:
        key = f.read()
        logger.logit(f"Read {keyfile}")
    key = key.encode() #converting it to bytes
    with open(filename, "r") as f:
        ciphertext = f.read()
        logger.logit(f"Read Cypher Text {filename}")
    ciphertext = bytes.fromhex(ciphertext)
    cipher = DES.new(key, DES.MODE_CBC)
    plaintext = cipher.decrypt(ciphertext)
    
    with open('RECOVERED_FILES/RES_recovery.txt', 'w') as f:
        f.write(plaintext.hex())
        logger.logit(f"Wrote to RECOVERED_FILES/RES_recovery.txt")

# def decryptt(keyfile,filename):
#     import base32hex
#     import hashlib
#     from Crypto.Cipher import DES
#     import logger
#     import util
#     with open(keyfile, 'r') as f:
#         key = f.read()
#         logger.logit(f"Read {keyfile}")
#     key = key.encode() #converting it to bytes
#     iv = b'constant'
#     crypter = DES.new(key, DES.MODE_CBC, iv)
#     with open(filename, "r") as f:
#         encrypted_string = f.read()
#         logger.logit(f"Read Cypher Text {filename}")
    
#     encrypted_string=base32hex.b32decode(encrypted_string)
#     decrypted_string = crypter.decrypt(encrypted_string)
#     with open('RECOVERED_FILES/RES_recovery.txt', 'w') as f:
#         f.write(decrypted_string.hex())
#         logger.logit(f"Wrote to RECOVERED_FILES/RES_recovery.txt")