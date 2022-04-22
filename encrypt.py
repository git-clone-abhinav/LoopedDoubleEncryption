import AES_encryptor
import AES_decryptor
import DES_encryptor
import DES_decryptor
import logger

logger.logit("====Start of Program====")
logger.logit("----AES Encryption Start----")

AES_encryptor.encrypt("rankers.txt")

logger.logit("----AES Encryption End----")
logger.logit("----DES Encryption Start----")

DES_encryptor.encrypt("AES_FILES/AES_cypher.cql")

logger.logit("----DES Encryption End----")
logger.logit("----DES Decryption Start----")

DES_decryptor.decrypt("DES_FILES/DES_key.key", "DES_FILES/DES_cypher.cql")

logger.logit("----DES Decryption End----")
logger.logit("----AES Decryption Start----")

AES_decryptor.decrypt("AES_FILES/AES_key.key", "RECOVERED_FILES/RES_recovery.txt")

logger.logit("----AES Decryption End----")
logger.logit("----End of Program----")

# logger.logit("Start of Program")
# logger.logit("AES Encryption Start")
# AES_encryptor.encrypt("rankers.txt")
# logger.logit("AES Encryption End")
# AES_decryptor.decrypt("AES_FILES/AES_key.key", "AES_FILES/AES_cypher.cql")
# logger.logit("AES Decryption End")
# logger.logit("End of Program")