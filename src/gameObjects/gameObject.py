
import importlib

def strToObjectClass(className):

    prefix = "src.gameObjects."
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(prefix+className)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, className)

    return c






class GameObject() :

    def __init__(self, name, x, y, tileInfo, properties) :

        self.name       = name
        self.x          = x
        self.y          = y
        self.active     = True
        self.tileId     = tileInfo[0]
        self.tile       = tileInfo[1]
        self.properties = properties


    def render(self, screen, tileSize) :

        if (self.active) :
            screen.blit(self.tile, (self.x * tileSize,  self.y * tileSize))





