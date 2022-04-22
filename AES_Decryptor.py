def decrypt(keyfile,filename):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad,pad
    import logger
    import util

    with open(keyfile, 'r') as f:
        key = f.read()
        logger.logit(f"Read {keyfile}")
    key = key.encode() #converting it to bytes

    with open(filename, "rb") as f:
        iv = f.read(16)
        cyphertext = f.read()
        logger.logit(f"Read Cypher Text {filename}")
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cyphertext = util.padmessage(cyphertext.hex())
    plaintext = unpad(cipher.decrypt(cyphertext.encode()), 16)

    with open('RECOVERED_FILES/recovered.txt', 'wb') as f:
        f.write(plaintext)
        logger.logit(f"Wrote to RECOVERED_FILES/rankers.txt")