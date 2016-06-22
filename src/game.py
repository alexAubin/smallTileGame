import sys

import pygame
import pygame.locals

class Game() : 


    def __init__(self, windowLabel = "My game", tileSize = 32) :

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


    def setMap(self, map) :

        self.map = map


    def setHero(self, hero) : 

        self.hero = hero

        # FIXME MAYBE ? Dirty weird tight coupling
        self.hero.mapLink = self.map


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
        self.map.render(self.screen, "bottom")
        
        if (self.hero.layer == 'middle') :
            self.hero.render(self.screen)
            self.map. render(self.screen, "top")
        else:
            self.map. render(self.screen, "top")
            self.hero.render(self.screen)

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
       
        moveDirection = ""
        if (keyPressed[pygame.K_UP])    : moveDirection = "back"
        if (keyPressed[pygame.K_DOWN])  : moveDirection = "front"
        if (keyPressed[pygame.K_LEFT])  : moveDirection = "left"
        if (keyPressed[pygame.K_RIGHT]) : moveDirection = "right"

        if (moveDirection != "") :
            self.hero.look(moveDirection)
            self.hero.move(moveDirection)




