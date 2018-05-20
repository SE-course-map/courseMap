import random
import string


def getRandomString(length):
    allowedLetters = \
        string.ascii_letters + \
        string.digits

    return ''.join(random.sample(allowedLetters, length))
