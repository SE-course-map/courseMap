from user import addUser
from login import generateSalt, hashPassword

kFirstUserName = 'admin'
kFirstUserPassword = '1111'

salt = generateSalt()
password = hashPassword(kFirstUserPassword, salt)

addUser(kFirstUserName, password, salt)