import pygame

class Projectile:
    
    def __init__(self, projectileStr, startingPos):
        self.projectileNumber = projectileStr
        self.x = startingPos[0]
        self.y = startingPos[1]
        str = "Assets\Projectiles\Laser Sprites\\" + projectileStr
        self.image = pygame.image.load(str)

    def draw(self, screen):
        self.x += 1
        screen.blit(self.image, (self.x, self.y))
