import pygame
from pygame.constants import MOUSEBUTTONDOWN
from UI.GameMenu.GameScreenPage import GameMenu
from UI.ShopPage import ShopMenu

class MainMenu:

    


    def drawText(text, font, color, surface, x, y):
        textObject = font.render(text, 1, color)
        textRec = textObject.get_rect()
        textRec.topleft = (x, y)
        surface.blit(textObject, textRec)

    def mainMenu(self):
        pygame.init()
        font = pygame.font.SysFont(None, 75)
        running = True
        click = False
        WINDOW_HEIGHT = 600
        WINDOW_WIDTH = 1000
        buttonHeight = 50
        buttonWidth = 200
        increaseSize = 10
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


        while(running):
            screen.fill((0, 0, 0))
            self.drawText("Pixel Siege", font, (255, 255, 255), screen, WINDOW_WIDTH/2 - 135, WINDOW_HEIGHT/4 - 10)

            mx, my = pygame.mouse.get_pos()

            startButton = pygame.Rect(WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT/2, buttonWidth, buttonHeight)
            shopButton = pygame.Rect(WINDOW_WIDTH/2 - 100, WINDOW_HEIGHT/2 + 100, buttonWidth, buttonHeight)

            if(startButton.collidepoint((mx, my))):
                startButton = pygame.Rect(WINDOW_WIDTH/2 - 105, WINDOW_HEIGHT/2 - 5, 
                    buttonWidth + increaseSize, buttonHeight + increaseSize)
                if(click):
                    GameMenu.gameMenu()
            if(shopButton.collidepoint((mx, my))):
                shopButton = pygame.Rect(WINDOW_WIDTH/2 - 105, WINDOW_HEIGHT/2 + 95, 
                    buttonWidth + increaseSize, buttonHeight + increaseSize)
                if(click):
                    ShopMenu.shopMenu()

            pygame.draw.rect(screen, (255, 0, 0), startButton)
            pygame.draw.rect(screen, (255, 0, 0), shopButton)

            click = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True

            pygame.display.update()