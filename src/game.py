import sys

import pygame
import pygame.locals

from view import View

class Game() : 


    def __init__(self, windowLabel = "My game", tileSize = 32) :

        # Initialize PyGame
        pygame.init()
   
        # Set up FPS clock
        self.fps = 30
        self.fpsClock = pygame.time.Clock()
        
        # Setup a view
        self.view = View(windowLabel, tileSize, (16,16))

        self.tileSize = tileSize


    def setMap(self, map) :

        self.map = map


    def setHero(self, hero) : 

        self.hero = hero
        self.hero.walkabilityChecker = self.map.getWalkability
        self.hero.getObject          = self.map.getObject

    def mainLoop(self) :

        # Handle events
        self.eventHandler()

        # Handle keys
        self.keysHandler()

        # Update character
        self.hero.update()

        # Center the view on hero
        self.view.setCenter((self.hero.x, self.hero.y))

        # Render elements
        self.view.render(self.map, self.hero)

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

        if (keyPressed[pygame.K_e]) :
            self.hero.actionKeyHandler();



