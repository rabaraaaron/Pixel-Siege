import sys
import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP


WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

class PauseLoop:

    def drawText(text, font, color, surface, x, y):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            textRec.center = (x, y)
            surface.blit(textObject, textRec)

    def pauseLoop(self, screen):

        bg = pygame.image.load("Assets/BG_PalmTree/destroyedTown.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        screen.blit(picture, (0, 0))
        paused = True
        click = False
        mouseLifted = False
        littleFont = pygame.font.SysFont(None, 28)
        littleButtonHeight = 25
        littleButtonWidth = 100
        littleButtonYPos = 10
        littleButtonXPos = WINDOW_WIDTH-110
        black = (0, 0, 0)
        white = (255, 255, 255)
        borderRadius = 5
        storedX, storedY = 0, 0


        while(paused):

            unpauseButton = pygame.Rect(littleButtonXPos, littleButtonYPos, littleButtonWidth, littleButtonHeight)
            restartButton = pygame.Rect(littleButtonXPos, littleButtonYPos+30, littleButtonWidth, littleButtonHeight)
            toMenuButton = pygame.Rect(littleButtonXPos, littleButtonYPos+60, littleButtonWidth, littleButtonHeight)

            mx, my = pygame.mouse.get_pos()

            if(unpauseButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, unpauseButton, 0, borderRadius)
                pygame.draw.rect(screen, black, restartButton, 0, borderRadius)
                pygame.draw.rect(screen, black, toMenuButton, 0, borderRadius)
                self.drawText("Resume", littleFont, black, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2)
                self.drawText("Restart", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+30)
                self.drawText("To Menu", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+60)
                if(click):
                    if(mouseLifted and unpauseButton.collidepoint((storedX, storedY))):
                        click = False
                        return 0
                    elif(mouseLifted):
                        click = False

            if(restartButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, unpauseButton, 0, borderRadius)
                pygame.draw.rect(screen, white, restartButton, 0, borderRadius)
                pygame.draw.rect(screen, black, toMenuButton, 0, borderRadius)
                self.drawText("Resume", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2)
                self.drawText("Restart", littleFont, black, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+30)
                self.drawText("To Menu", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+60)
                if(click):
                    if(mouseLifted and restartButton.collidepoint((storedX, storedY))):
                        click = False
                        return 1
                    elif(mouseLifted):
                        click = False

            if(toMenuButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, unpauseButton, 0, borderRadius)
                pygame.draw.rect(screen, black, restartButton, 0, borderRadius)
                pygame.draw.rect(screen, white, toMenuButton, 0, borderRadius)
                self.drawText("Resume", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2)
                self.drawText("Restart", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+30)
                self.drawText("To Menu", littleFont, black, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+60)
                if(click):
                    if(mouseLifted and toMenuButton.collidepoint((storedX, storedY))):
                        click = False
                        return 2
                    elif(mouseLifted):
                        click = False

            if(not unpauseButton.collidepoint((mx, my)) and not restartButton.collidepoint((mx, my)) and not toMenuButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, unpauseButton, 0, borderRadius)
                pygame.draw.rect(screen, black, restartButton, 0, borderRadius)
                pygame.draw.rect(screen, black, toMenuButton, 0, borderRadius)
                self.drawText("Resume", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2)
                self.drawText("Restart", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+30)
                self.drawText("To Menu", littleFont, white, screen, littleButtonXPos+littleButtonWidth/2, littleButtonYPos+littleButtonHeight/2+60)

            mouseLifted = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True
                        storedX, storedY = pygame.mouse.get_pos()
                if(event.type == MOUSEBUTTONUP):
                    if(event.button == 1):
                        mouseLifted = True

            pygame.display.update()