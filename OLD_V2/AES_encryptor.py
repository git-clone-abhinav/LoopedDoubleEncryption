def encrypt(filename):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import util
    import logger

    key = util.keygen(16)
    with open('AES_FILES/AES_key.txt', 'w') as f:
        f.write(key)
        logger.logit("Written AES key to file")
    key = key.encode()
    IV = b"This is an IV456"
    cypher = AES.new(key, AES.MODE_CBC,IV)

    with open(filename, "rb") as f:
        plaintext = f.read()
        logger.logit(f"Read text form {filename}")

    cypher_text = cypher.encrypt(pad(plaintext, AES.block_size))

    with open('AES_FILES/AES_cypher.txt', 'w') as f:
        f.write(cypher_text.hex())
        logger.logit("Written AES Cypher Text to file")