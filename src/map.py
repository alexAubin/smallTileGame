
import sys
import json
import pygame
import pygame.locals


# Dummy pokeball class for object layer test
class Pokeball :

    def __init__(self, name, x, y, tileId, properties) :

        pass


def strToClass(className):
    
    try :
        return getattr(sys.modules[__name__], className)
    except AttributeError :
        raise NameError("Class '%s' doesn't exist." % className)




class Map() :



    def __init__(self, tileset, mapJsonPath) :

        self.tileset = tileset

        self.layers = self.load(mapJsonPath)



    def load(self, mapJsonPath) :
        
        with open(mapJsonPath) as f :

            mapJson = json.load(f)

        self.layer  = {}
        self.width  = mapJson["width"]
        self.height = mapJson["height"]

        for layer in mapJson["layers"] :
            
            layerName = layer["name"]
            
            if (layer["type"] == "tilelayer") :
                layerData = layer["data"]
            else :
                layerData = self.makeObjectLayer(layer["objects"], self.width, self.height)

            self.layer[layerName] = layerData



    def makeObjectLayer(self, data, mapWidth, mapHeight) :

        objectLayer = []

        for i in range(0,mapWidth * mapHeight) :
            objectLayer.append(None)

        for obj in data :

            x = int(obj["x"]) / int(obj["width"])
            y = int(obj["y"]) / int(obj["width"])
            
            tileId     = obj["gid"]
            objType    = obj["type"]
            properties = obj["properties"]
            name       = obj["name"]

            theObj = strToClass(objType)(name, x, y, tileId, properties)        

            objectLayer[x + y * mapWidth] = theObj

        return objectLayer




    def getWalkability(self, x, y) :

        tileIdBot = self.layer["bot"][y*self.width+x] - 1
        tileIdTop = self.layer["top"][y*self.width+x] - 1
      
        return (self.tileset.mask[tileIdBot], self.tileset.mask[tileIdTop])



    def render(self, screen, layerName) :

        layerToRender = self.layer[layerName]

        for (i, tileId) in enumerate(layerToRender) :

            x = i % self.width
            y = i / self.width

            tileId = tileId - 1

            if (tileId != -1) : 
                screen.blit(self.tileset.tiles[tileId], 
                            (x*self.tileset.tileSize,
                             y*self.tileset.tileSize))



