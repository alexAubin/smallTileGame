import sys

import pygame
import pygame.locals

class Game() : 


    def __init__(self, windowLabel = "My game", tileSize = 32) :

        print "In init"

        # Initialize PyGame
        pygame.init()
   
        # Set up FPS clock
        self.fps = 30
        self.fpsClock = pygame.time.Clock()

        # Set up window
        self.screen = pygame.display.set_mode((20*tileSize, 23*tileSize), 0, 32)
        pygame.display.set_caption(windowLabel)

        # Init layers
        self.layers = []

        self.tileSize = tileSize


    def setHero(self, hero) : 

        self.hero = hero


    def addMapLayer(self, layer) :

        self.layers.append(layer)
        

    def mainLoop(self) :

        # Handle events
        self.eventHandler()

        # Handle keys
        self.keysHandler()

        # Update character
        self.hero.update()

        # Clean screen
        self.screen.fill( (0,0,0) )
       
        # Render elements
        self.layers[0].render(self.screen)
        
        if (self.hero.layer == 'middle') :
            self.hero.     render(self.screen)
            self.layers[1].render(self.screen)
        else:
            self.layers[1].render(self.screen)
            self.hero.     render(self.screen)

        # Update screen
        pygame.display.update()
        self.fpsClock.tick(self.fps)
        


    def eventHandler(self) :

        for event in pygame.event.get():

            if (event.type == pygame.QUIT) :
                pygame.quit()
                sys.exit()


    def keysHandler(self) :
        
        keyPressed = pygame.key.get_pressed()
       
        if (keyPressed[pygame.K_UP]
        or keyPressed[pygame.K_DOWN]
        or keyPressed[pygame.K_LEFT]
        or keyPressed[pygame.K_RIGHT]) :

            if (self.hero.moving != "") :
                return
            else :
                maskTileTop = self.layers[1].getTileWalkability(self.hero.x, self.hero.y)
                if (maskTileTop == '0') :
                    self.hero.layer = 'top'


            if (keyPressed[pygame.K_UP])    : 
                dx =  0
                dy = -1
                d = "back"
            if (keyPressed[pygame.K_DOWN])  : 
                dx =  0
                dy = +1
                d = "front"
            if (keyPressed[pygame.K_LEFT])  : 
                dx = -1
                dy =  0
                d = "left"
            if (keyPressed[pygame.K_RIGHT]) : 
                dx = +1
                dy =  0
                d = "right"

            self.hero.look(d)
            
            maskNextTileBot = self.layers[0].getTileWalkability(self.hero.x+dx, self.hero.y+dy)
            maskNextTileTop = self.layers[1].getTileWalkability(self.hero.x+dx, self.hero.y+dy)
           
            if (maskNextTileBot == '1') or (maskNextTileTop == '1') :
                return
            
            if (maskNextTileTop == '2') :
                self.hero.layer = 'middle'

            self.hero.move(d)




