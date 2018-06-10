from abc import ABC, abstractmethod, abstractstaticmethod

class AbstractEssence(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractstaticmethod
    def getFromForm():
        pass
