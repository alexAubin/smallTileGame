import pygame
import pygame.locals


class Character() :


    def __init__(self, spritePath, spritePosition, spriteWidth, spriteHeight, initPosition) :

        self.loadSprite(spritePath, spriteWidth, spriteHeight, spritePosition)

        self.x = initPosition[0]
        self.y = initPosition[1]
        self.w = spriteWidth
        self.h = spriteHeight
        self.orientation       = "front"
        self.currentSpriteStep = 0
        self.moving            = ""
        self.layer             = 'middle'

        self.updateCurrentSprite()


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
        
        #if (layer == "bottom") :
        #    offset = 16
        #else :
        #    offset = 0
        #toDraw = self.currentSprite.subsurface((0, offset, 32, 32))
        
        # Uuuuuuh FIXME
        screen.blit(self.currentSprite, (self.x * 32,  self.y * 32 - 16))


    def look(self, direction) :

        self.orientation = direction
        
        self.updateCurrentSprite()

    def move(self, direction) :

        if (self.moving != "") : return

        self.moving     = direction
        self.movingStep = 0

    def update(self) :

        if   (self.moving == "back") :
            self.y = self.y - 1/9.0
        elif (self.moving == "front") :
            self.y = self.y + 1/9.0
        elif (self.moving == "left") :
            self.x = self.x - 1/9.0
        elif (self.moving == "right") :
            self.x = self.x + 1/9.0
        else :
            return
        
        self.movingStep = self.movingStep + 1
        
        self.currentSpriteStep = int(self.movingStep / 3)

        if (self.currentSpriteStep == 3) : 
            self.currentSpriteStep = 0
            self.moving = ""
            self.x = int(round(self.x))
            self.y = int(round(self.y))

        self.updateCurrentSprite()
            
    def updateCurrentSprite(self):
        
        self.currentSprite = self.sprites[self.orientation][self.currentSpriteStep]

