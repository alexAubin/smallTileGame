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


    def render(self, view) :
       
        view.blitTile(self.currentSprite, (self.x,  self.y - 0.5))


    def look(self, direction) :

        if (self.moving != "") : return

        self.orientation = direction
        
        self.updateCurrentSprite()

    def move(self, direction) :

        if (self.moving != "") : return

        if (self.tileIsWalkable(direction) == False) : return

        self.moving     = direction
        self.movingStep = 0
        self.updateCurrentLayer()

    def actionKeyHandler(self) :

        # Ignore the action key if character is currently moving
        if (self.moving != "") :
            return

        if   (self.orientation == "back" ) : dx, dy =  0, -1
        elif (self.orientation == "front") : dx, dy =  0, +1
        elif (self.orientation == "left" ) : dx, dy = -1, 0
        elif (self.orientation == "right") : dx, dy = +1, 0

        obj = self.getObject(self.x+dx, self.y+dy)

        if (obj == None) : 
            return
        else :
            obj.triggerAction()

    def update(self) :

        if (self.moving == "") :
            return
        else :
            self.nextMovingStep()

    def nextMovingStep(self) :

        if   (self.moving == "back") :
            self.y = self.y - 1/9.0
        elif (self.moving == "front") :
            self.y = self.y + 1/9.0
        elif (self.moving == "left") :
            self.x = self.x - 1/9.0
        elif (self.moving == "right") :
            self.x = self.x + 1/9.0
        
        self.movingStep = self.movingStep + 1
        
        self.currentSpriteStep = int(self.movingStep / 3)

        if (self.currentSpriteStep == 3) : 
            self.currentSpriteStep = 0
            self.moving = ""
            self.x = int(round(self.x))
            self.y = int(round(self.y))
            self.updateCurrentLayer()

        self.updateCurrentSprite()

    def tileIsWalkable(self, direction) :

        if   (direction == "back" ) : dx, dy =  0, -1
        elif (direction == "front") : dx, dy =  0, +1
        elif (direction == "left" ) : dx, dy = -1, 0
        elif (direction == "right") : dx, dy = +1, 0

        maskNextTile = self.walkabilityChecker(self.x+dx, self.y+dy)

        if (1 in maskNextTile) :
            return False
        else :
            return True
 

    def updateCurrentLayer(self) :

        if (self.moving == "") :

            maskTileTop = self.walkabilityChecker(self.x, self.y)[2]
            if (maskTileTop == 0) : self.layer = 'top'

        else :

            if   (self.moving == "back" ) : dx, dy =  0, -1
            elif (self.moving == "front") : dx, dy =  0, +1
            elif (self.moving == "left" ) : dx, dy = -1, 0
            elif (self.moving == "right") : dx, dy = +1, 0

            maskNextTileTop = self.walkabilityChecker(self.x+dx, self.y+dy)[2]
           
            if (maskNextTileTop == 2) : self.layer = 'middle'


    def updateCurrentSprite(self) :
        
        self.currentSprite = self.sprites[self.orientation][self.currentSpriteStep]

