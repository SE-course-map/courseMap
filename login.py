import string
import random
import hashlib


def generateSalt():
    """
    Generates random salt

    Returns:
         str: 32 letters of randomly generated salt
            for hashing a password
    """
    allowedLetters = string.ascii_letters + \
                     string.digits + \
                     string.punctuation
    kSaltLength = 32
    return ''.join(random.sample(allowedLetters, kSaltLength))


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


def checkPassword(rawPassword, hashedPassword, salt):
    """
    Check if user's password corresponds with hashed one

    Args:
         rawPassword (str): password prompted by user
         hashedPassword (str):
         salt (str):

    Returns:
          bool: whether check was successfull
    """
    return hashedPassword == hashPassword(rawPassword, salt)


if __name__ == '__main__':
    salt = generateSalt()
    print("salt:", salt)

    rawPassword = 'password'
    print("raw password:", rawPassword)

    hashedPassword = hashPassword(rawPassword, salt)
    print("hash password:", hashedPassword)

    print("Checking true", checkPassword(rawPassword, hashedPassword, salt))
    print("Checking false", checkPassword("notMyPassword", hashedPassword, salt))