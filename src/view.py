import sys

import pygame
import pygame.locals

class View() : 


    def __init__(self, windowLabel = "My game", tileSize = 32, widthAndHeight = (10,10)) :

        self.width, self.height = widthAndHeight
        
        self.screen = pygame.display.set_mode( (self.width  * tileSize, 
                                                self.height * tileSize), 0, 32)
        pygame.display.set_caption(windowLabel)

        self.tileSize = tileSize
        self.offset   = (0,0)


    def setCenter(self, position) :

        (center_x, center_y) = position
        offset_x = center_x - self.width  / 2 + 0.5
        offset_y = center_y - self.height / 2 + 0.5

        self.offset = (offset_x, offset_y)

    def render(self, theMap, theHero) :

        # Clean screen
        self.screen.fill( (0,0,0) )
        
        
        theMap.renderLayer(self, "bot")
        theMap.renderLayer(self, "objects")
        
        if (theHero.layer == 'middle') :
            theHero.render(self)
            theMap .renderLayer(self, "top")
        else:
            theMap .renderLayer(self, "top")
            theHero.render(self)

    def blitTile(self, tile, position) :

        (tile_x   , tile_y  ) = position
        (offset_x , offset_y) = self.offset

        tile_x_on_view = tile_x - offset_x
        tile_y_on_view = tile_y - offset_y

        self.screen.blit(tile, (tile_x_on_view * self.tileSize, 
                               tile_y_on_view * self.tileSize))



