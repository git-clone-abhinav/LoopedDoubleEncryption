def decrypt(keyfile,filename):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad,pad
    import logger
    import util

    with open(keyfile, 'r') as f:
        key = f.read()
        logger.logit(f"Read {keyfile}")
    key = key.encode() #converting it to bytes

    with open(filename,'rb') as f:
        cyphertext = f.read()
        logger.logit(f"Read Cypher Text {filename}")
    IV = b"This is an IV456"
    cipher = AES.new(key, AES.MODE_CBC, IV)
    # cyphertext = util.padmessage(cyphertext)
    plaintext = cipher.decrypt(cyphertext)
    plaintext = plaintext.hex()
    with open('RECOVERED_FILES/recovered.txt', 'w') as f:
        f.write(plaintext)
        logger.logit(f"Wrote to RECOVERED_FILES/rankers.txt")