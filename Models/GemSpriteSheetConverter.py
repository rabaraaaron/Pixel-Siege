import pygame
import json

class GemSpriteSheetConverter:

    def __init__(self, fileName):
        self.fileName = fileName
        self.metaData = self.fileName.replace('png', 'json')
        with open(self.metaData) as f:
            self.data = json.load(f)
        self.zoom = self.data['zoom']
        self.xOffset = self.data['xOffset']
        self.yOffset = self.data['yOffset']
        self.spriteSheet = pygame.transform.rotozoom(pygame.image.load(self.fileName).convert(), 0, self.zoom)
        f.close()

    def getSprite(self, x, y, w, h):
        black = (0, 0, 0)
        white = (255, 255, 255)
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey(black)
        sprite.blit(self.spriteSheet, (0, 0), (x, y, w, h))
        return sprite

    def parseSprite(self):
        sprite = self.data['currency']['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.getSprite(x, y, w, h)
        return image
