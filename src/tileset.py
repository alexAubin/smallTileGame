
import pygame
import pygame.locals
from PIL import Image


class Tileset() :


    def __init__(self, tileSize, tilesetImagePath, tilesetMaskPath) :

        self.tileSize = tileSize

        self.loadTilesetImage(tilesetImagePath)
        self.loadTilesetMask (tilesetMaskPath)
    
    def loadTilesetImage(self, path) :

        tilesetImage = pygame.image.load(path)
        self.tilesetWidth, self.tilesetHeight = tilesetImage.get_size()
        
        self.tiles = []

        for tileY in range(0, self.tilesetHeight / self.tileSize):
            for tileX in range(0, self.tilesetWidth / self.tileSize):

                tile = (tileX * self.tileSize, tileY * self.tileSize, 
                                self.tileSize,         self.tileSize)
                
                self.tiles.append(tilesetImage.subsurface(tile))

    def loadTilesetMask(self, path) :

        im = Image.open(path)
        pix = im.load()
        
        self.mask = [ ]

        for y in range(0, self.tilesetHeight / self.tileSize) :
        
            row = []
    
            for x in range(0, self.tilesetWidth / self.tileSize) :

                (r, g, b, a) = pix[ (x+0.5)*self.tileSize, (y+0.5)*self.tileSize]

                # Transparent = walkable
                if   (a == 0) : row.append(0)
                # Black = block
                elif (r == 0) : row.append(1)
                # Else / white = walkable by behind
                else          : row.append(2)

            self.mask.extend(row)
