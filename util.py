import string
import random

def keygen(length):
    # choose from all lowercase letter
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def padmessage(message):
    # padding the message with ' '
    message = message + (b' ' * (16 - len(message) % 16))
    return message