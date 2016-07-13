

from gameObject import GameObject as GameObject



class Pokeball(GameObject) :

    def __init__(self, name, x, y, tileInfo, properties) :

        GameObject.__init__(self,name,x,y,tileInfo,properties)

    def render(self, screen, tileSize) :
 
        screen.blit(self.tile, (self.x * tileSize,  self.y * tileSize))





