import json
import pygame
import math

from pygame import mouse

class Projectile:
    
    def __init__(self, projectileStr, color, startingPos, mousePos, power):
        self.projectileNumber = projectileStr
        self.x = startingPos[0]
        self.y = startingPos[1]
        str = "Assets\Projectiles\\" + color + "\\" + projectileStr
        self.metaData = str.replace('png', 'json')
        with open(self.metaData) as f:
            self.data = json.load(f)
        self.width = self.data['width']
        self.height = self.data['height']
        self.image = pygame.image.load(str)
        self.power = power
        self.mousePos = mousePos
        self.angle = 0
        self.startingX = startingPos[0]
        self.startingY = startingPos[1]
        self.time = 0
        f.close()
        

    def projectilePath(self, screen):

        self.time += .12
        gravity = 9.81
        vx = self.power * math.cos(self.angle)
        vy = self.power * math.sin(self.angle)
        newX = self.startingX + vx*self.time
        newY = self.startingY - (vy*self.time - .5*gravity*(self.time**2))

        self.x = newX
        self.y = newY

        black = (0, 0, 0)
        screen.blit(self.image, (self.x-40, self.y-50))


    def findAngle(self):

        sX = self.x
        sY = self.y
        rX = self.mousePos[0]
        rY = self.mousePos[1]

        try:
            angle = math.atan((sY - rY) / (sX - rX))
        except:
            angle = (math.pi / 2) * 3

        if rY < sY and rX > sX:
            angle = abs(angle)
        elif rY < sY and rX < sX:
            angle = math.pi - angle
        elif rY > sY and rX < sX:
            angle = math.pi + abs(angle)
        elif rY > sY and rX > sX:
            angle = (math.pi * 2) - angle

        if(angle == 0.0):
            angle = math.pi
        self.angle = angle
