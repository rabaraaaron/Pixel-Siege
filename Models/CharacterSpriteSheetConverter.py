import pygame
import json

class CharacterSpriteSheetConverter:


    def __init__(self, fileName):
        self.fileName = fileName
        self.metaData = self.fileName.replace('png', 'json')
        with open(self.metaData) as f:
            self.data = json.load(f)
        f.close()
        self.zoom = self.data['zoom']
        self.spriteSheet = pygame.transform.rotozoom(pygame.image.load(self.fileName).convert_alpha(), 0, self.zoom)
        self.attackColor = self.data['color']
        self.speed = self.data["speed"]
        self.projectileColor = self.data['projectileColor']


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

    def getHoldFrame(self):
        return self.data['hold']

    def getAttackColor(self):
        return self.attackColor
