import sys
import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from UI.GameMenu.GameScreenPage import GameMenu

class MainMenuSelection:

    def drawText(text, font, color, surface, x, y):
        textObject = font.render(text, 1, color)
        textRec = textObject.get_rect()
        textRec.center = (x, y)
        surface.blit(textObject, textRec)

    def mainMenuSelection(self):
        pygame.init()
        bigFont = pygame.font.SysFont(None, 75)
        littleFont = pygame.font.SysFont(None, 28)
        running = True
        click = False
        mouseLifted = False
        WINDOW_HEIGHT = 600
        WINDOW_WIDTH = 1000
        storyAndSurvivalButtonHeight = 50
        storyAndSurvivalButtonWidth = 200
        black = (0, 0, 0)
        white = (255, 255, 255)
        borderRadius = 5
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        bg = pygame.image.load("Assets/BG_PalmTree/wreckage.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        firstButtonHeight = WINDOW_HEIGHT/2
        secondButtonHeight = WINDOW_HEIGHT/2+75
        halfWindowWidth = WINDOW_WIDTH/2
        backButtonHeight = 20
        backButtonWidth = 80
        backButtonYPos = 10
        backButtonXPos = WINDOW_WIDTH-90
        littleFont = pygame.font.SysFont(None, 28)


        while(running):
            screen.blit(picture, (0, 0))

            mx, my = pygame.mouse.get_pos()

            storyModeButton = pygame.Rect(halfWindowWidth - 100, firstButtonHeight, storyAndSurvivalButtonWidth, storyAndSurvivalButtonHeight)
            survivalModeButton = pygame.Rect(halfWindowWidth - 100, secondButtonHeight, storyAndSurvivalButtonWidth, storyAndSurvivalButtonHeight)
            backButton = pygame.Rect(backButtonXPos, backButtonYPos, backButtonWidth, backButtonHeight)


            if(storyModeButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, backButton, 0, borderRadius)
                self.drawText("Story Mode",littleFont, black, screen, halfWindowWidth, firstButtonHeight+storyAndSurvivalButtonHeight/2)
                self.drawText("Survival Mode",littleFont, white, screen, halfWindowWidth, secondButtonHeight+storyAndSurvivalButtonHeight/2)
                self.drawText("Back", littleFont, white, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)                                
                if(click):
                    mx, my = pygame.mouse.get_pos()
                    if(mouseLifted and storyModeButton.collidepoint((mx, my))):
                        GameMenu.gameMenu(GameMenu)
                        click = False
                    elif(mouseLifted):
                        click = False

            if(survivalModeButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, white, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, backButton, 0, borderRadius) 
                self.drawText("Story Mode",littleFont, white, screen, halfWindowWidth, firstButtonHeight+storyAndSurvivalButtonHeight/2)
                self.drawText("Survival Mode",littleFont, black, screen, halfWindowWidth, secondButtonHeight+storyAndSurvivalButtonHeight/2)
                self.drawText("Back", littleFont, white, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)                
                if(click):
                    mx, my = pygame.mouse.get_pos()
                    if(mouseLifted and survivalModeButton.collidepoint((mx, my))):
                        print("Survival mode selected")
                        click = False
                    elif(mouseLifted):
                        click = False

            if(backButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, white, backButton, 0, borderRadius) 
                self.drawText("Story Mode", littleFont, white, screen, halfWindowWidth, firstButtonHeight + storyAndSurvivalButtonHeight/2)
                self.drawText("Survival Mode",littleFont, white, screen, halfWindowWidth, secondButtonHeight+storyAndSurvivalButtonHeight/2)                
                self.drawText("Back", littleFont, black, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)               
                if(click):
                    mx, my = pygame.mouse.get_pos()
                    if(mouseLifted and backButton.collidepoint((mx, my))):
                        running = False
                        click = False
                    elif(mouseLifted):
                        click = False
                    

            if(not storyModeButton.collidepoint((mx, my)) and not survivalModeButton.collidepoint((mx, my)) and not backButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, backButton, 0, borderRadius) 
                self.drawText("Story Mode",littleFont, white, screen, halfWindowWidth, firstButtonHeight+storyAndSurvivalButtonHeight/2)
                self.drawText("Survival Mode",littleFont, white, screen, halfWindowWidth, secondButtonHeight+storyAndSurvivalButtonHeight/2)
                self.drawText("Back", littleFont, white, screen, backButtonXPos+backButtonWidth/2, backButtonYPos+backButtonHeight/2)

            mouseLifted = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True
                if(event.type == MOUSEBUTTONUP):
                    if(event.button == 1):
                        mouseLifted = True

            pygame.display.update()