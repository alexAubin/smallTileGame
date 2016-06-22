
import csv
import pygame
import pygame.locals


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

        self.mask = []

        with open(path, 'rb') as f :

            reader = csv.reader(f)

            for row in reader :

                self.mask.extend(map(int, row))



