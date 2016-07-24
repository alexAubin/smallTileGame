

from gameObject import GameObject as GameObject



class Pokeball(GameObject) :



    def __init__(self, name, x, y, tileInfo, properties) :

        GameObject.__init__(self,name,x,y,tileInfo,properties)



    def render(self, screen, tileSize) :

        GameObject.render(self, screen, tileSize)


    def triggerAction(self) :

        if (self.active) :

            self.active = False
            self.tileId = -1
            print "Hero looted a Pokeball !"
