import json
import pickle
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame
import sys

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 75)

class RoundCompletionPage:

    def drawText(text, font, color, surface, x, y):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            textRec.center = (x, y)
            surface.blit(textObject, textRec)
    
    def roundComplete(self):

        try:
            with open('SaveData.p', 'rb') as handle:
                b = pickle.load(handle)
            level = b['level']
            characterName = b['characterPath']
            gems = b['gems']
            handle.close()
            print("loaded save file")
        except:
            print("error loading the saveData.p in the round completion")

        jsonToRead = "level"+str(level)
        with open("Models\\Levels\\"+jsonToRead+".json", 'r+') as f:
            levelData = json.load(f)
        level = levelData['level']
        gemsEarnedPerKill = levelData['gemsPerKill']
        enemyAmount = levelData['round']['totalAmount']


        running = True
        click = False
        mouseLifted = False
        bg = pygame.image.load("Assets/BG_PalmTree/marsh.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        borderRadius = 5
        black = (0, 0, 0)
        white = (255, 255, 255)
        littleFont = pygame.font.SysFont(None, 28)
        bigButtonHeight = 25
        bigButtonWidth = 100
        halfWindowWidth = WINDOW_WIDTH/2
        firstButtonHeight = WINDOW_HEIGHT/2
        storedX, storedY = 0, 0


        while(running):
            screen.blit(picture, (0, 0))
            mx, my = pygame.mouse.get_pos()

            continueButton = pygame.Rect(halfWindowWidth - 125, firstButtonHeight, bigButtonWidth, bigButtonHeight)
            menuButton = pygame.Rect(halfWindowWidth + 25, firstButtonHeight, bigButtonWidth, bigButtonHeight)

            message = "Completed level: " + str(level)
            self.drawText(message, font, black, screen, halfWindowWidth, WINDOW_HEIGHT/10)
            message = "You Earned: " + str(gemsEarnedPerKill * enemyAmount) + " Gems"
            self.drawText(message, littleFont, black, screen, halfWindowWidth, WINDOW_HEIGHT/6)

            if(continueButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, continueButton, 0, borderRadius)
                pygame.draw.rect(screen, black, menuButton, 0, borderRadius)

                self.drawText("Continue", littleFont, black, screen, halfWindowWidth-75, firstButtonHeight + bigButtonHeight/2)
                self.drawText("To Menu", littleFont, white, screen, halfWindowWidth+75, firstButtonHeight + bigButtonHeight/2)

                if(click):
                    if(mouseLifted and continueButton.collidepoint((storedX, storedY))):
                        running = False
                        return 0
                    elif(mouseLifted):
                        click = False

                        
            if(menuButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, continueButton, 0, borderRadius)
                pygame.draw.rect(screen, white, menuButton, 0, borderRadius)

                self.drawText("Continue", littleFont, white, screen, halfWindowWidth-75, firstButtonHeight + bigButtonHeight/2)
                self.drawText("To Menu", littleFont, black, screen, halfWindowWidth+75, firstButtonHeight + bigButtonHeight/2)

                if(click):
                    if(mouseLifted and menuButton.collidepoint((storedX, storedY))):
                        running = False
                        return 1
                    elif(mouseLifted):
                        click = False
            
            if(not continueButton.collidepoint((mx, my)) and not menuButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, continueButton, 0, borderRadius)
                pygame.draw.rect(screen, black, menuButton, 0, borderRadius)
                self.drawText("Continue", littleFont, white, screen, halfWindowWidth-75, firstButtonHeight + bigButtonHeight/2)
                self.drawText("To Menu", littleFont, white, screen, halfWindowWidth+75, firstButtonHeight + bigButtonHeight/2)

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