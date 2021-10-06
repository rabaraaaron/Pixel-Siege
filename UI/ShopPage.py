from pygame.constants import MOUSEBUTTONDOWN
import pygame
import sys

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 75)

class ShopMenu:
    
    def shopMenu():
        running = True
        click = False

        def drawText(text, font, color, surface, x, y):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            textRec.topleft = (x, y)
            surface.blit(textObject, textRec)

        while(running):

            screen.fill((0, 0, 0))
            drawText("Shop menu", font, (255, 255, 255), screen, WINDOW_WIDTH/2 - 135, WINDOW_HEIGHT/4 - 10)

            mx, my = pygame.mouse.get_pos()

            startButton = pygame.Rect(WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT/2, 200, 50)
            shopButton = pygame.Rect(WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT/2 + 100, 200, 50)

            if(startButton.collidepoint((mx, my))):
                if(click):
                    running = False
            if(shopButton.collidepoint((mx, my))):
                if(click):
                    running = False

            pygame.draw.rect(screen, (255, 0, 0), startButton)
            pygame.draw.rect(screen, (255, 0, 0), shopButton)

            click = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True

            pygame.display.update()