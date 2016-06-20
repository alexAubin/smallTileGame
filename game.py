import sys
import csv

import pygame
import pygame.locals


class Character() :


    def __init__(self, spritePath, spritePosition, spriteWidth, spriteHeight, initPosition) :

        self.loadSprite(spritePath, spriteWidth, spriteHeight, spritePosition)

        self.x = initPosition[0]
        self.y = initPosition[1]
        self.orientation   = "front"
        self.currentSprite = self.sprites[self.orientation][0]
        self.moving        = ""
        self.w = spriteWidth
        self.h = spriteHeight


    def loadSprite(self, path, w, h, position) :

        self.sprites          = {}
        self.sprites["front"] = []
        self.sprites["right"] = []
        self.sprites["left"]  = []
        self.sprites["back"]  = []
        
        spritesImage = pygame.image.load(path)
        spritesWidth, spritesHeight = spritesImage.get_size()
       
        for i in range(0, 3) :
            self.sprites["front"].append(self.getSprite(spritesImage, w,h, i, position))
        for i in range(3, 6) :
            self.sprites["back"] .append(self.getSprite(spritesImage, w,h, i, position))
        for i in range(6, 9) :
            self.sprites["right"].append(self.getSprite(spritesImage, w,h, i, position))
        for i in range(9,12) :
            self.sprites["left"] .append(self.getSprite(spritesImage, w,h, i, position))


    def getSprite(self, spritesImage, w,h, i, j) :
       
        return spritesImage.subsurface((i * w, (j-1) * h, w, h))


    def render(self, screen) :
                                                # Uuuuuuh FIXME
        screen.blit(self.currentSprite, (self.x * 32,  self.y * 32 - 16))


    def move(self, direction) :

        if (self.moving != "") : return

        self.moving     = direction
        self.movingStep = 0

        if   (direction == "forward" ) : self.orientation = "back"
        elif (direction == "backward") : self.orientation = "front"
        elif (direction == "left")     : self.orientation = "left"
        elif (direction == "right")    : self.orientation = "right"

    def update(self) :

        if   (self.moving == "forward") :
            self.y = self.y - 1/9.0
        elif (self.moving == "backward") :
            self.y = self.y + 1/9.0
        elif (self.moving == "left") :
            self.x = self.x - 1/9.0
        elif (self.moving == "right") :
            self.x = self.x + 1/9.0
        else :
            return
        
        self.movingStep = self.movingStep + 1
        
        spriteId   = int(self.movingStep / 3)

        if (spriteId == 3) : 
            spriteId = 0
            self.moving = ""
            self.x = int(round(self.x))
            self.y = int(round(self.y))


        self.currentSprite = self.sprites[self.orientation][spriteId]
            


class Map() :


    def __init__(self, tilesetPath, tileSize, layerPathList) :

        self.tileSize = tileSize

        self.loadTileset(tilesetPath)
        self.loadLayers(layerPathList)
    

    def loadLayers(self, layerPathList) :

        self.layers = [ ]
        
        for layerPath in layerPathList :
    
            # Reader this layer from csv file

            layer = [ ]
        
            with open(layerPath, 'rb') as f :
                
                reader = csv.reader(f)
                for row in reader : layer.append(row)

            # Append this layer to the layer list

            self.layers.append(layer)

    

    def loadTileset(self, path) :

        tilesetImage = pygame.image.load(path)
        tilesetWidth, tilesetHeight = tilesetImage.get_size()
        
        self.tileset = []

        for tileY in range(0, tilesetHeight / self.tileSize):
            for tileX in range(0, tilesetWidth / self.tileSize):

                tile = (tileX * self.tileSize, tileY * self.tileSize, 
                                self.tileSize,         self.tileSize)
                
                self.tileset.append(tilesetImage.subsurface(tile))

    def update(self) :

        pass


    def render(self, screen) :
        
        for layer in self.layers :
            for (y, row) in enumerate(layer) :
                for (x, tileId) in enumerate(row) :
       
                    # FIXME : should move this to when the CSV is loaded
                    tileId = int(tileId)

                    if (tileId != -1) : 
                        screen.blit(self.tileset[tileId], (x*self.tileSize,
                                                           y*self.tileSize))



colors = { 
           "black" : ( 0,  0,  0 ), 
           "white" : (255,255,255)
         }



class MyGame() : 




    def __init__(self, windowLabel = "My game") :

        print "In init"

        # Initialize PyGame
        pygame.init()
   
        # Set up FPS clock
        self.fps = 30
        self.fpsClock = pygame.time.Clock()

        # Set up window
        self.screen = pygame.display.set_mode((20*32, 20*32), 0, 32)
        pygame.display.set_caption(windowLabel)


    def mainLoop(self, character, stuffToRender) :


        # Handle events
        self.eventHandler()

        # Handle keys
        self.keysHandler(character)

        # Clean screen
        self.screen.fill(colors["black"])
       
        # Render elements
        for stuff in stuffToRender :
            stuff.update()
            stuff.render(self.screen)
        
        # Update screen
        pygame.display.update()
        self.fpsClock.tick(self.fps)
        



    def eventHandler(self) :

        for event in pygame.event.get():

            if (event.type == pygame.QUIT) :
                pygame.quit()
                sys.exit()




    def keysHandler(self, character) :
        
        keyPressed = pygame.key.get_pressed()

        if (keyPressed[pygame.K_UP])    : character.move("forward")
        if (keyPressed[pygame.K_DOWN])  : character.move("backward") 
        if (keyPressed[pygame.K_LEFT])  : character.move("left")
        if (keyPressed[pygame.K_RIGHT]) : character.move("right")











def main() :



    myGame = MyGame("test");

    m = Map("assets/tileset.png", 32, [ "map_layer1.csv", "map_layer2.csv" ])
    p = Character("assets/sprites_trainers.png", 4, 32, 48, (10,10))

    while True :
        myGame.mainLoop( p,  [ m, p ] );

main()
