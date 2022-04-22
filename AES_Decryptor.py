def decrypt(keyfile,filename):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    import logger

    with open(keyfile, 'r') as f:
        key = f.read()
        logger.logit(f"Read {keyfile}")
    key = key.encode() #converting it to bytes

    with open(filename, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()
        logger.logit(f"Read Cypher Test {filename}")
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    with open('RECOVERED_FILES/recovered.txt', 'wb') as f:
        f.write(plaintext)
        logger.logit(f"Wrote to RECOVERED_FILES/rankers.txt")