import OLD_V2.AES_encryptor as AES_encryptor
import OLD_V2.AES_decryptor as AES_decryptor
import DES_encryptor as DES_encryptor
import DES_decryptor as DES_decryptor
import logger

logger.logit("====Start of Program====")
logger.logit("----AES Encryption Start----")

AES_encryptor.encrypt("rankers.txt")

logger.logit("----AES Encryption End----")
logger.logit("----DES Encryption Start----")

DES_encryptor.encrypt("AES_FILES/AES_cypher.txt")

logger.logit("----DES Encryption End----")
logger.logit("----DES Decryption Start----")

DES_decryptor.decrypt("DES_FILES/DES_key.txt", "DES_FILES/DES_cypher.txt")

logger.logit("----DES Decryption End----")
logger.logit("----AES Decryption Start----")

AES_decryptor.decrypt("AES_FILES/AES_key.txt", "RECOVERED_FILES/RES_recovery.txt")

logger.logit("----AES Decryption End----")
logger.logit("----End of Program----")

# logger.logit("Start of Program")
# logger.logit("AES Encryption Start")
# AES_encryptor.encrypt("rankers.txt")
# logger.logit("AES Encryption End")
# AES_decryptor.decrypt("AES_FILES/AES_key.key", "AES_FILES/AES_cypher.cql")
# logger.logit("AES Decryption End")
# logger.logit("End of Program")