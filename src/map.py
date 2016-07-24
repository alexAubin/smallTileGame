
import sys
import json
import types
import pygame
import pygame.locals

from gameObjects import gameObject

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
            properties = obj.get("properties",None)
            name       = obj["name"]

            if (objType == "heroStart") :
                self.heroStart = (x,y)
            else :
                c = gameObject.strToObjectClass(objType)
                y = y - 1
                theObj = c(name, x, y, (tileId, self.tileset.tiles[tileId - 1]), properties)
                objectLayer[x + y * mapWidth] = theObj

        return objectLayer




    def getWalkability(self, x, y) :

        i = x + y*self.width
        tileIdBot    = self.layer["bot"][i]           - 1
        if (self.layer["objects"][i] != None) :
            tileIdObject = self.layer["objects"][i].tileId - 1
        else : 
            tileIdObject = 0
        tileIdTop    = self.layer["top"][i]           - 1

        return (self.tileset.mask[tileIdBot],
                self.tileset.mask[tileIdObject],
                self.tileset.mask[tileIdTop])

    def getObject(self, x, y) :

        i = x + y*self.width
        return self.layer["objects"][i];



    def render(self, screen, layerName) :

        layerToRender = self.layer[layerName]

        for (i, tileId) in enumerate(layerToRender) :

            x = i % self.width
            y = i / self.width

            if (type(tileId) == int) :

                tileId = tileId - 1

                if (tileId != -1) :
                    screen.blit(self.tileset.tiles[tileId],
                                (x*self.tileset.tileSize,
                                 y*self.tileset.tileSize))


            else :

                if (tileId == None) : continue

                tileId.render(screen, self.tileset.tileSize);

