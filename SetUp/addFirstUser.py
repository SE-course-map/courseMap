import os
import sys

projectRootDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

sys.path.append(projectRootDirectory)
os.chdir(projectRootDirectory)

from json import loads

from Controller.UserController import UserController
from Essence.User import User

jsonFile = open("SetUp/UserCredentials.json", "r")

userData = loads(jsonFile.read())

UserController().add(User(userData['userName'], userData['password']))