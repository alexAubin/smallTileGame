
import importlib

def strToObjectClass(className):

    prefix = "src.gameObjects."
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(prefix+className)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, className)

    return c






class GameObject() :

    def __init__(self, name, x, y, tileId, properties) :

        self.name = name
        self.x    = x
        self.y    = y
        self.tileId     = tileId
        self.properties = properties





