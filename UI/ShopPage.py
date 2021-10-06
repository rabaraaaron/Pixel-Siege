from pygame.constants import MOUSEBUTTONDOWN
import pygame
import sys

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 75)

class ShopMenu:

    def drawText(text, font, color, surface, x, y):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            textRec.center = (x, y)
            surface.blit(textObject, textRec)
    
    def shopMenu(self):
        running = True
        click = False
        black = (0, 0, 0)
        white = (255, 255, 255)
        bg = pygame.image.load("Assets/BG_PalmTree/cyberpunkShop.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        backButtonYPos = 10
        backButtonXPos = WINDOW_WIDTH-90
        backButtonHeight = 20
        backButtonWidth = 80
        littleFont = pygame.font.SysFont(None, 28)

        

        while(running):

            screen.blit(picture, (0, 0))

            mx, my = pygame.mouse.get_pos()

            backButton = pygame.Rect(backButtonXPos, backButtonYPos, backButtonWidth, backButtonHeight)


            if(backButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, backButton)
                self.drawText("Back", littleFont, black, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)
                if(click):
                    running = False
            else:
                pygame.draw.rect(screen, black, backButton)
                self.drawText("Back", littleFont, white, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)


            click = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True

            pygame.display.update()