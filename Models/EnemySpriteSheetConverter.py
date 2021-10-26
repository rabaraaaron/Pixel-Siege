import pygame
import json

class EnemySpriteSheetConverter:

    def __init__(self, fileName):
        self.fileName = fileName
        self.metaData = self.fileName.replace('png', 'json')
        with open(self.metaData) as f:
            self.data = json.load(f)
        self.zoom = self.data['zoom']
        self.spriteSheet = pygame.transform.rotozoom(pygame.image.load(self.fileName).convert(), 0, self.zoom)
        self.w, self.h = self.data['actualWidth'], self.data['actualHeight']
        self.hitboxOffsetX = self.data["hitboxOffsetX"]
        self.hitboxOffsetY = self.data["hitboxOffsetY"]
        self.yOffscreen = self.data["yOffscreen"]
        self.multiplyer = self.data['damageMultiplyer']
        self.attackFrame = self.data['attackFrame']
        self.selfDestruct = self.data['selfDestruct']
        f.close()

    def getSprite(self, x, y, w, h):
        black = (0, 0, 0)
        white = (255, 255, 255)
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey(black)
        sprite.blit(self.spriteSheet, (0, 0), (x, y, w, h))
        return sprite


    def parseSprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.getSprite(x, y, w, h)
        return image

    def getFrameNames(self):
        frames = []
        for x in self.data['frames'] :
            frames.append(x)
        return frames

    def getFrameSize(self):
        return self.data['size']

    def getSpeed(self):
        return self.data['speed']
    
    def getWidthHeight(self):
        return (self.w, self.h)

    def getMultiplyer(self):
        return self.multiplyer

    def getDamage(self):
        return self.data['attack']

    def getHealthBarOffset(self):
        return (self.data['healthBarOffsetX'], self.data['healthBarOffsetY'])