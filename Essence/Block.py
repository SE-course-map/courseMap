from flask import request

from Common.Exceptions import *
from Essence.AbstractEssence import *

kMinBlockNameLength = 4
kBlockColorLength = 7


class Block(AbstractEssence):
    @staticmethod
    def getFromForm():
        try:
            return Block(request.form['name'], request.form['color'])
        except Exception as e:
            raise FormException(str(e))

    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color

    def validate(self):
        if len(self.name) < kMinBlockNameLength:
            raise NameLengthException("Block Name is too short")
        if len(self.color) != kBlockColorLength or self.color[0] != '#':
            raise ColorLengthException("Invalid Color value")
        try:
            int(self.color[1:], 16)
        except ValueError as e:
            raise ColorLengthException("Invalid Color value")
