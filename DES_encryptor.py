def encrypt(filename):
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import pad
    import util
    import logger

    key = util.keygen(8)
    with open('DES_FILES/DES_key.key', 'w') as f:
        f.write(key)
        logger.logit("Written DES key to file")
    key = key.encode()

    cypher = DES.new(key, DES.MODE_ECB)

    with open(filename, 'rb') as f:
        AES_cypher_text = f.read()
        logger.logit(f"Read text form {filename}")
    
    cypher_text = cypher.encrypt(pad(AES_cypher_text, 8))

    with open('DES_FILES/DES_cypher.cql', 'wb') as f:
        f.write(cypher_text)
        logger.logit("Written DES Cypher Text to file")
