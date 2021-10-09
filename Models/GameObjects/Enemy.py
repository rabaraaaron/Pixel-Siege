import pygame

from Models.EnemySpriteSheetConverter import EnemySpriteSheetConverter


class Enemy:

    def __init__(self, x, y, name, fileName):
        self.x = x
        self.y = y
        self.flying = False
        self.fileName = fileName
        self.attacking = False
        self.index = 0
        self.converter = EnemySpriteSheetConverter(self.fileName)
        list = self.converter.getFrameNames()
        self.animationList = []
        for x in list:
            self.animationList.append(pygame.transform.flip(self.converter.parseSprite(x), True, False))

    def hasBeenHit(self):
        pass

    def drawPosition(self, fName):

        self.fileName = fName
        self.index = 0
        self.converter = EnemySpriteSheetConverter(fName)
        list = self.converter.getFrameNames()
        self.holdFrame = self.converter.getHoldFrame()
        self.animationList = []
        for x in list:
            self.animationList.append(self.converter.parseSprite(x))

    def updatePosition(self):
        if self.attacking:
            self.x += 5
        else:
            self.x -= 5

    def checkDirection(self):
        if self.x < 120:
            self.attacking = True
            print("changed to attacking")



        

    