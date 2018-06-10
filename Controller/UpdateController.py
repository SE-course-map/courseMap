from Controller.AbstractController import *

class UpdateController(AbstractController):
    @abstractstaticmethod
    def update(id, newEssence):
        pass
