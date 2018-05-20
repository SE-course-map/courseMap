import hashlib

from Common.Common import getRandomString


def generateSalt():
    """
    Generates random salt
    Returns:
         str: 32 letters of randomly generated salt
            for hashing a password
    """
    kSaltLength = 32

    return getRandomString(kSaltLength)


def hashPassword(rawPassword, salt):
    """
    Hashes user's password by using md5 hash function
    Args:
        rawPassword (str): password prompted by user
        salt (str): salt that corresponds to user
    Returns:
        str: 32 letters of md5 hash
    """
    m = hashlib.md5()
    m.update((rawPassword + salt).encode('utf-8'))
    return m.hexdigest()
