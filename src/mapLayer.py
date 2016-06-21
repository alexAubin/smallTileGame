
import csv
import pygame
import pygame.locals


class MapLayer() :


    def __init__(self, tilesetPaths, tileSize, layerPath) :

        self.tileSize = tileSize

        tilesetImagePath = tilesetPaths[0]
        tilesetMaskPath  = tilesetPaths[1]

        self.loadTilesetImage(tilesetImagePath)
        self.loadTilesetMask (tilesetMaskPath)
        self.load(layerPath)
    

    def load(self, layerPath) :

        self.layer = [ ]
        
        with open(layerPath, 'rb') as f :
            
            reader = csv.reader(f)
            
            for row in reader : 
                self.layer.append(row)


    def loadTilesetImage(self, path) :

        tilesetImage = pygame.image.load(path)
        self.tilesetWidth, self.tilesetHeight = tilesetImage.get_size()
        
        self.tileset = []

        for tileY in range(0, self.tilesetHeight / self.tileSize):
            for tileX in range(0, self.tilesetWidth / self.tileSize):

                tile = (tileX * self.tileSize, tileY * self.tileSize, 
                                self.tileSize,         self.tileSize)
                
                self.tileset.append(tilesetImage.subsurface(tile))

    def loadTilesetMask(self, path) :

        self.tilesetMask = []

        with open(path, 'rb') as f :

            reader = csv.reader(f)

            for row in reader :

                self.tilesetMask.extend(row)


    def getTileWalkability(self, x, y) :

        tileId = self.layer[int(y)][int(x)]

        return self.tilesetMask[int(tileId)]

    def render(self, screen) :
        
        for (y, row) in enumerate(self.layer) :

            for (x, tileId) in enumerate(row) :
   
                # FIXME : should move this to when the CSV is loaded
                tileId = int(tileId)

                if (tileId != -1) : 
                    screen.blit(self.tileset[tileId], (x*self.tileSize,
                                                       y*self.tileSize))



