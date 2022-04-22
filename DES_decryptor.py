def decrypt(keyfile,filename):
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import unpad
    import logger

    with open(keyfile, 'r') as f:
        key = f.read()
        logger.logit(f"Read {keyfile}")
    key = key.encode() #converting it to bytes

    with open(filename, "rb") as f:
        ciphertext = f.read()
        logger.logit(f"Read Cypher Text {filename}")
    
    cipher = DES.new(key, DES.MODE_CBC)
    plaintext = cipher.decrypt(ciphertext).rstrip()
    
    with open('RECOVERED_FILES/RES_recovery.txt', 'wb') as f:
        f.write(plaintext)
        logger.logit(f"Wrote to RECOVERED_FILES/RES_recovery.txt")