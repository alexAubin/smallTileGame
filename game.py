import sys
import csv

import pygame
import pygame.locals


class Character() :


    def __init__(self, spritePath, spriteSize, spritePosition, initPosition) :

        self.loadSprite(spritePath, spriteSize, spritePosition)

        self.x = initPosition[0]
        self.y = initPosition[1]
        self.orientation   = "front"
        self.currentSprite = self.sprites[self.orientation][0]
        self.moving        = ""


    def loadSprite(self, path, size, position) :

        self.sprites          = {}
        self.sprites["front"] = []
        self.sprites["right"] = []
        self.sprites["left"]  = []
        self.sprites["back"]  = []
        
        spritesImage = pygame.image.load(path)
        spritesWidth, spritesHeight = spritesImage.get_size()
       
        for i in range(0, 4) :
            self.sprites["front"].append(self.getSprite(spritesImage, size, i, position))
        for i in range(4, 8) :
            self.sprites["right"].append(self.getSprite(spritesImage, size, i, position))
        for i in range(8, 12) :
            self.sprites["left"] .append(self.getSprite(spritesImage, size, i, position))
        for i in range(12,16) :
            self.sprites["back"] .append(self.getSprite(spritesImage, size, i, position))


    def getSprite(self, spritesImage, size, i, j) :
        
        return spritesImage.subsurface((i * size, (j-1) * size, size, size))


    def render(self, screen) :
                                                # Uuuuuuh FIXME
        screen.blit(self.currentSprite, (self.x * 32,  self.y * 32))


    def move(self, direction) :

        if (self.moving != "") : return

        self.moving     = direction
        self.movingFrom = (self.x, self.y)

        if   (direction == "forward" ) : self.orientation = "back"
        elif (direction == "backward") : self.orientation = "front"
        elif (direction == "left")     : self.orientation = "left"
        elif (direction == "right")    : self.orientation = "right"

    def update(self) :

        if   (self.moving == "forward") :
            self.y = self.y - 0.1
            p      = self.y
            p_init = self.movingFrom[1]
        elif (self.moving == "backward") :
            self.y = self.y + 0.1
            p      = self.y
            p_init = self.movingFrom[1]
        elif (self.moving == "left") :
            self.x = self.x - 0.1
            p      = self.x
            p_init = self.movingFrom[0]
        elif (self.moving == "right") :
            self.x = self.x + 0.1
            p      = self.x
            p_init = self.movingFrom[0]
        else :
            return
        
        spriteId = abs(int((p - int(p_init)) * 4.0))

        if (spriteId == 4) : 
            spriteId = 0
            self.moving = ""

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
    p = Character("assets/sprites.png", 32, 6, (10,10))

    while True :
        myGame.mainLoop( p,  [ m, p ] );

main()
