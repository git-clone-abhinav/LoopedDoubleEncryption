import string
import random

def keygen(length):
    # choose from all lowercase letter
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def padmessage(message):
    while len(message) % 16 != 0:
        message += ' '
    return message