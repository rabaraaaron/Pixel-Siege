import json
import pickle
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame
import sys

from Models.GemSpriteSheetConverter import GemSpriteSheetConverter

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 75)

class RoundCompletionPage:

    def drawText(text, font, color, surface, x, y, center):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            if center:
                textRec.center = (x, y)
            else:
                textRec.topLeft = (x, y)
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
        messageBoardWidth = 250
        messageBoardHeight = 300
        halfWindowWidth = WINDOW_WIDTH/2
        firstButtonHeight = (WINDOW_HEIGHT/4) * 3
        storedX, storedY = 0, 0


        while(running):
            screen.blit(picture, (0, 0))
            mx, my = pygame.mouse.get_pos()

            continueButton = pygame.Rect(halfWindowWidth - 125, firstButtonHeight, bigButtonWidth, bigButtonHeight)
            menuButton = pygame.Rect(halfWindowWidth + 25, firstButtonHeight, bigButtonWidth, bigButtonHeight)

            messagebackground = pygame.Rect(halfWindowWidth - messageBoardWidth/2, WINDOW_HEIGHT/5, messageBoardWidth, messageBoardHeight)
            pygame.draw.rect(screen, black, messagebackground, 0, borderRadius)
            messageForeground = pygame.Rect(halfWindowWidth - messageBoardWidth/2 + 4, WINDOW_HEIGHT/5 + 4, messageBoardWidth - 8, messageBoardHeight - 8)
            pygame.draw.rect(screen, white, messageForeground, 0, borderRadius)

            message = "Completed level: " + str(level)
            self.drawText(message, font, black, screen, halfWindowWidth, WINDOW_HEIGHT/10, True)
            message = "You Earned: " + str(gemsEarnedPerKill * enemyAmount)
            self.drawText(message, littleFont, black, screen, halfWindowWidth, WINDOW_HEIGHT/5 + 20, True)

            gem = GemSpriteSheetConverter("Assets\Currency\gems.png")
            screen.blit(gem.parseSprite(), (halfWindowWidth + gem.xOffset, WINDOW_HEIGHT/5 + gem.yOffset))

            if(continueButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, continueButton, 0, borderRadius)
                pygame.draw.rect(screen, black, menuButton, 0, borderRadius)

                self.drawText("Continue", littleFont, black, screen, halfWindowWidth-75, firstButtonHeight + bigButtonHeight/2, True)
                self.drawText("To Menu", littleFont, white, screen, halfWindowWidth+75, firstButtonHeight + bigButtonHeight/2, True)

                if(click):
                    if(mouseLifted and continueButton.collidepoint((storedX, storedY))):
                        running = False
                        return 0
                    elif(mouseLifted):
                        click = False

                        
            if(menuButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, continueButton, 0, borderRadius)
                pygame.draw.rect(screen, white, menuButton, 0, borderRadius)

                self.drawText("Continue", littleFont, white, screen, halfWindowWidth-75, firstButtonHeight + bigButtonHeight/2, True)
                self.drawText("To Menu", littleFont, black, screen, halfWindowWidth+75, firstButtonHeight + bigButtonHeight/2, True)

                if(click):
                    if(mouseLifted and menuButton.collidepoint((storedX, storedY))):
                        running = False
                        return 1
                    elif(mouseLifted):
                        click = False
            
            if(not continueButton.collidepoint((mx, my)) and not menuButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, continueButton, 0, borderRadius)
                pygame.draw.rect(screen, black, menuButton, 0, borderRadius)
                self.drawText("Continue", littleFont, white, screen, halfWindowWidth-75, firstButtonHeight + bigButtonHeight/2, True)
                self.drawText("To Menu", littleFont, white, screen, halfWindowWidth+75, firstButtonHeight + bigButtonHeight/2, True)

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