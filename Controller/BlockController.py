from Essence.Block import *
from Connection.Connection import *
from Controller.UpdateController import *


class BlockController(UpdateController):
    @staticmethod
    def add(block):
        block.validate()

        with CourseMapConnection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """ INSERT INTO block (name, color) VALUES (%s, %s) """,
                (block.name, block.color)
            )

    @staticmethod
    def getAll():
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" SELECT id, name, color FROM block """)
            return cursor.fetchall()

    @staticmethod
    def remove(blockId):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" DELETE FROM block WHERE id=%s """, (blockId,))

    @staticmethod
    def update(blockId, newBlock):
        newBlock.validate()
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """ UPDATE block SET name=%s, color=%s WHERE id=%s""",
                (newBlock.name, newBlock.color, blockId)
            )
