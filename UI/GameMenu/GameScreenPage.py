from pygame.constants import MOUSEBUTTONDOWN
import pygame
import sys

from UI.GameMenu.OptionsLoop import OptionsLoop

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 75)

class GameMenu:
    
    def gameMenu():
        running = True
        click = False
        bg = pygame.image.load("Assets/BG_PalmTree/field.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        buttonHeight = 50
        buttonWidth = 200
        increaseSize = 10

        def drawText(text, font, color, surface, x, y):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            textRec.topleft = (x, y)
            surface.blit(textObject, textRec)


        while(running):
            screen.blit(picture, (0, 0))

            mx, my = pygame.mouse.get_pos()

            pauseButton = pygame.Rect(WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT/2, buttonWidth, buttonHeight)
            

            if(pauseButton.collidepoint((mx, my))):
                pauseButton = pygame.Rect(WINDOW_WIDTH/2 - 105, WINDOW_HEIGHT/2 - 5, 
                    buttonWidth + increaseSize, buttonHeight + increaseSize)
                if(click):
                    running = OptionsLoop.pauseLoop(screen)

            pygame.draw.rect(screen, (255, 0, 0), pauseButton)

            click = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True

            pygame.display.update()