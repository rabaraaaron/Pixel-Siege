import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from UI.GameMenu.GameScreenPage import GameMenu
from UI.ShopPage import ShopMenu
from UI.MainMenu.MainMenuSelection import MainMenuSelection

class MainMenu:

    def drawText(text, font, color, surface, x, y):
        textObject = font.render(text, 1, color)
        textRec = textObject.get_rect()
        textRec.center = (x, y)
        surface.blit(textObject, textRec)

    def mainMenu(self):
        pygame.init()
        bigFont = pygame.font.SysFont(None, 75)
        littleFont = pygame.font.SysFont(None, 28)
        running = True
        click = False
        mouseLifted = False
        WINDOW_HEIGHT = 600
        WINDOW_WIDTH = 1000
        buttonHeight = 50
        buttonWidth = 200
        black = (0, 0, 0)
        white = (255, 255, 255)
        borderRadius = 5
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        bg = pygame.image.load("Assets/BG_PalmTree/wreckage.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        firstButtonHeight = WINDOW_HEIGHT/2
        secondButtonHeight = WINDOW_HEIGHT/2+75
        halfWindowWidth = WINDOW_WIDTH/2

        while(running):
            screen.blit(picture, (0, 0))
            self.drawText("Pixel Siege", bigFont, black, screen, halfWindowWidth, WINDOW_HEIGHT/3)

            mx, my = pygame.mouse.get_pos()

            startButton = pygame.Rect(halfWindowWidth - 100, firstButtonHeight, buttonWidth, buttonHeight)
            shopButton = pygame.Rect(halfWindowWidth - 100, secondButtonHeight, buttonWidth, buttonHeight)

            if(startButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, startButton, 0, borderRadius)
                pygame.draw.rect(screen, black, shopButton, 0, borderRadius)
                self.drawText("Play",littleFont, black, screen, halfWindowWidth, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, white, screen, halfWindowWidth, secondButtonHeight+buttonHeight/2)
                if(click):
                    mx, my = pygame.mouse.get_pos()
                    if(mouseLifted and startButton.collidepoint((mx, my))):
                        MainMenuSelection.mainMenuSelection(MainMenuSelection)
                        click = False
                    elif(mouseLifted):
                        click = False

            if(shopButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, startButton, 0, borderRadius)
                pygame.draw.rect(screen, white, shopButton, 0, borderRadius)
                self.drawText("Play",littleFont, white, screen, halfWindowWidth, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, black, screen, halfWindowWidth, secondButtonHeight+buttonHeight/2)
                if(click):
                    mx, my = pygame.mouse.get_pos()
                    if(mouseLifted and shopButton.collidepoint((mx, my))):
                        ShopMenu.shopMenu(ShopMenu)
                        click = False
                    elif(mouseLifted):
                        click = False
                    

            if(not startButton.collidepoint((mx, my)) and not shopButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, startButton, 0, borderRadius)
                pygame.draw.rect(screen, black, shopButton, 0, borderRadius)
                self.drawText("Play",littleFont, white, screen, halfWindowWidth, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, white, screen, halfWindowWidth, secondButtonHeight+buttonHeight/2)
            
            mouseLifted = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True
                if(event.type == MOUSEBUTTONUP):
                    if(event.button == 1):
                        mouseLifted = True

            pygame.display.update()