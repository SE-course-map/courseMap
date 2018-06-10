from abc import ABC, abstractstaticmethod

class AbstractController(ABC):
    @abstractstaticmethod
    def add(essence):
        pass

    @abstractstaticmethod
    def remove(id):
        pass

    @abstractstaticmethod
    def getAll():
        pass
