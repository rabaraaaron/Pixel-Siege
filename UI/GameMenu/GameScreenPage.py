from pygame.constants import MOUSEBUTTONDOWN
import pygame
import sys
from UI.GameMenu.OptionsLoop import OptionsLoop
from UI.GameMenu.StoryMode import StoryMode

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 75)

class GameMenu:

    def drawText(text, font, color, surface, x, y):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            textRec.center = (x, y)
            surface.blit(textObject, textRec)
    
    def gameMenu(self):
        running = True
        click = False
        mouseLifted = True
        bg = pygame.image.load("Assets/BG_PalmTree/destroyedTown.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        borderRadius = 5
        black = (0, 0, 0)
        white = (255, 255, 255)
        littleFont = pygame.font.SysFont(None, 28)
        bigButtonHeight = 50
        bigButtonWidth = 200
        halfWindowWidth = WINDOW_WIDTH/2
        firstButtonHeight = WINDOW_HEIGHT/2
        backButtonHeight = 20
        backButtonWidth = 80
        backButtonYPos = 10
        backButtonXPos = WINDOW_WIDTH-90


        while(running):
            screen.blit(picture, (0, 0))
            mx, my = pygame.mouse.get_pos()

            playButton = pygame.Rect(halfWindowWidth - 100, firstButtonHeight, bigButtonWidth, bigButtonHeight)
            backButton = pygame.Rect(backButtonXPos, backButtonYPos, backButtonWidth, backButtonHeight)
            

            if(playButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, playButton, 0, borderRadius)
                pygame.draw.rect(screen, black, backButton, 0, borderRadius)
                self.drawText("Begin", littleFont, black, screen, halfWindowWidth, firstButtonHeight + bigButtonHeight/2)
                self.drawText("Back", littleFont, white, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)
                if(click):
                    mx, my = pygame.mouse.get_pos()
                    if(mouseLifted and playButton.collidepoint((mx, my))):
                        StoryMode.play(screen)
                        click = False
                    elif(mouseLifted):
                        click = False

            if(backButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, playButton, 0, borderRadius)
                pygame.draw.rect(screen, white, backButton, 0, borderRadius) 
                self.drawText("Begin", littleFont, white, screen, halfWindowWidth, firstButtonHeight + bigButtonHeight/2)
                self.drawText("Back", littleFont, black, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)               
                if(click):
                    mx, my = pygame.mouse.get_pos()
                    if(mouseLifted and backButton.collidepoint((mx, my))):
                        running = False
                        click = False
                    elif(mouseLifted):
                        click = False


            if(not playButton.collidepoint((mx, my)) and not backButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, playButton, 0, borderRadius)
                pygame.draw.rect(screen, black, backButton, 0, borderRadius)
                self.drawText("Begin", littleFont, white, screen, halfWindowWidth, firstButtonHeight + bigButtonHeight/2)
                self.drawText("Back", littleFont, white, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)

            mouseLifted = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True
                        mouseLifted = True
                

            pygame.display.update()