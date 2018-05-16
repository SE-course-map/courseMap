import string
import random
import hashlib


def generateSalt():
    allowedLetters = string.ascii_letters + \
                     string.digits + \
                     string.punctuation
    kSaltLength = 32
    return ''.join(random.sample(allowedLetters, kSaltLength))


def hashPassword(rawPassword, salt):
    m = hashlib.md5()
    m.update((rawPassword + salt).encode('utf-8'))
    return m.hexdigest()


def checkPassword(rawPassword, hashedPassword, salt):
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