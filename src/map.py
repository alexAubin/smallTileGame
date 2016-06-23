
import csv
import pygame
import pygame.locals


class Map() :


    def __init__(self, tileset, layerBottom, layerTop) :

        self.tileset = tileset

        self.layerBottom = self.load(layerBottom)
        self.layerTop    = self.load(layerTop)
    

    def load(self, layerPath) :

        layer = [ ]
        
        with open(layerPath, 'rb') as f :
            
            reader = csv.reader(f)
            
            for row in reader : 
                layer.append(map(int,row))

        return layer


    def getWalkability(self, x, y) :


        tileIdBot = self.layerBottom[y][x]
        tileIdTop = self.layerTop   [y][x]
        
        return (self.tileset.mask[tileIdBot], self.tileset.mask[tileIdTop])

    def render(self, screen, layerName) :
        
        if (layerName == "bottom") : layerToRender = self.layerBottom
        if (layerName == "top")    : layerToRender = self.layerTop

        for (y, row) in enumerate(layerToRender) :

            for (x, tileId) in enumerate(row) :
   
                if (tileId != -1) : 
                    screen.blit(self.tileset.tiles[tileId], 
                                (x*self.tileset.tileSize,
                                 y*self.tileset.tileSize))



