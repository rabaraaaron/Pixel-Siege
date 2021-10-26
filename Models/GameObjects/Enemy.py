import pygame

from Models.EnemySpriteSheetConverter import EnemySpriteSheetConverter


class Enemy:

    def __init__(self, x, y, fileName):
        
        self.flying = False
        self.fileName = fileName
        self.attacking = False
        self.index = 0
        self.converter = EnemySpriteSheetConverter(self.fileName)
        
        self.x = x
        self.y = y - self.converter.yOffscreen
        list = self.converter.getFrameNames()
        self.animationList = []
        self.speed = self.converter.getSpeed()
        for x in list:
            self.animationList.append(pygame.transform.flip(self.converter.parseSprite(x), True, False))
        self.w, self.h = self.converter.getWidthHeight()
        self.hitboxOffsetX, self.hitboxOffsetY = self.converter.hitboxOffsetX, self.converter.hitboxOffsetY
        self.multiplyer = self.converter.getMultiplyer()
        self.health = 100
        self.damage = self.converter.getDamage()
        self.healthBarOffsetX, self.healthBarOffsetY = self.converter.getHealthBarOffset()
        self.attackFrame = self.converter.attackFrame
        self.selfDestruct = self.converter.selfDestruct

    def takeDamage(self, damage):
        self.health -= damage

    def drawPosition(self, fName):

        self.fileName = fName
        self.index = 0
        self.converter = EnemySpriteSheetConverter(fName)
        list = self.converter.getFrameNames()
        self.holdFrame = self.converter.getHoldFrame()
        self.animationList = []
        for x in list:
            self.animationList.append(self.converter.parseSprite(x))
        self.w, self.h = self.converter.getWidthHeight()

    def updatePosition(self):
        if not self.attacking:
            self.x -= self.speed

    def checkPosition(self):

        if self.x < 90 and not self.attacking:
            self.attacking = True
            self.fileName = self.fileName.replace("walk", "attack")
            self.index = 0
            self.converter = EnemySpriteSheetConverter(self.fileName)
            self.w = self.converter.w
            self.h = self.converter.h
            self.hitboxOffsetX = self.converter.hitboxOffsetX
            self.hitboxOffsetY = self.converter.hitboxOffsetY
            list = self.converter.getFrameNames()
            self.animationList = []
            for x in list:
                self.animationList.append(pygame.transform.flip(self.converter.parseSprite(x), True, False))

    def hitBy(self, projectileCoords, projectileWidth, projectileHeight):
        if(projectileCoords[0] > self.x+self.hitboxOffsetX and projectileCoords[0] < self.x+self.w+self.hitboxOffsetX) or (projectileCoords[0] + projectileWidth > self.x+self.hitboxOffsetX and projectileCoords[0] + projectileWidth < self.x+self.w+self.hitboxOffsetX):
            if(projectileCoords[1] > self.y+self.hitboxOffsetY and projectileCoords[1] < self.y+self.h+self.hitboxOffsetY) or ((projectileCoords[1] + projectileHeight > self.y+self.hitboxOffsetY and projectileCoords[1] + projectileHeight < self.y+self.h+self.hitboxOffsetY)):
                return True
        return False






        

    