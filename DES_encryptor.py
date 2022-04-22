def encrypt(filename):
    from Crypto.Cipher import DES
    from Crypto.Util.Padding import pad
    import util
    import logger

    key = util.keygen(8)
    with open('DES_FILES/DES_key.txt', 'w') as f:
        f.write(key)
        logger.logit("Written DES key to file")
    key = key.encode()
    cypher = DES.new(key, DES.MODE_ECB)

    with open(filename, 'r') as f:
        AES_cypher_text = f.read()
        logger.logit(f"Read text form {filename}")
    AES_cypher_text = AES_cypher_text.encode()
    cypher_text = cypher.encrypt(pad(AES_cypher_text, 8))

    with open('DES_FILES/DES_cypher.txt', 'w') as f:
        f.write(cypher_text.hex())
        logger.logit("Written DES Cypher Text to file")

def encryptt(filename):
    import base32hex
    import logger,util
    from Crypto.Cipher import DES

    key = util.keygen(8)
    with open('DES_FILES/DES_key.txt', 'w') as f:
        f.write(key)
        logger.logit("Written DES key to file")
    key = key.encode()
    iv = b'constant'
    crypter = DES.new(key, DES.MODE_CBC, iv)

    with open(filename, 'r') as f:
        AES_cypher_text = f.read()
        logger.logit(f"Read text form {filename}")
    plain_text = AES_cypher_text.encode()
    plain_text += b'\x00' * (8 - len(plain_text) % 8)
    ciphertext = crypter.encrypt(plain_text)
    encode_string= base32hex.b32encode(ciphertext)
    with open('DES_FILES/DES_cypher.txt', 'w') as f:
        f.write(encode_string)
        logger.logit("Written DES Cypher Text to file")