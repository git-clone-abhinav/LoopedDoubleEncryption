def encrypt(filename):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import util
    import logger

    key = util.keygen(16)
    with open('AES_FILES/AES_key.key', 'w') as f:
        f.write(key)
        logger.logit("Written AES key to file")
    key = key.encode()

    cypher = AES.new(key, AES.MODE_CBC)

    with open(filename, "rb") as f:
        plaintext = f.read()
        logger.logit(f"Read text form {filename}")

    cypher_text = cypher.encrypt(pad(plaintext, AES.block_size))

    with open('AES_FILES/AES_cypher.cql', 'wb') as f:
        f.write(cypher_text)
        logger.logit("Written AES Cypher Text to file")