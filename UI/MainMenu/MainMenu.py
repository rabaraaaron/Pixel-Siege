import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from UI.GameMenu.GameScreenPage import GameMenu
from UI.ShopPage import ShopMenu


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
        fourthWindowWidth = WINDOW_WIDTH/4 + 40
        storedX, storedY = 0, 0

        fade = 1000
        pygame.mixer.init()
        pygame.mixer.music.load('Assets\Sounds\MainMenu.wav')
        pygame.mixer.music.play(loops=-1)


        while(running):
            screen.blit(picture, (0, 0))
            self.drawText("Pixel Siege", bigFont, black, screen, halfWindowWidth, WINDOW_HEIGHT/3)
            

            mx, my = pygame.mouse.get_pos()

            storyModeButton = pygame.Rect(fourthWindowWidth, firstButtonHeight, buttonWidth, buttonHeight)
            survivalModeButton = pygame.Rect(halfWindowWidth, firstButtonHeight, buttonWidth, buttonHeight)
            shopButton = pygame.Rect(fourthWindowWidth, secondButtonHeight, buttonWidth, buttonHeight)
            optionsButton = pygame.Rect(halfWindowWidth, secondButtonHeight, buttonWidth, buttonHeight)


            if(storyModeButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, shopButton, 0, borderRadius)
                pygame.draw.rect(screen, black, optionsButton, 0, borderRadius)
                self.drawText("Story Mode",littleFont, black, screen, fourthWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Survival Mode",littleFont, white, screen, halfWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                self.drawText("Options",littleFont, white, screen, halfWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                
                if(click):
                    if(mouseLifted and storyModeButton.collidepoint((storedX, storedY))):
                        pygame.mixer.music.load('Assets\Sounds\Effects\whoosh.wav')
                        pygame.mixer.music.play(loops=-1)
                        pygame.mixer.music.fadeout(fade)
                        GameMenu.gameMenu(GameMenu)
                        pygame.mixer.music.load('Assets\Sounds\MainMenu.wav')
                        pygame.mixer.music.play(loops=-1)
                        click = False
                    elif(mouseLifted):
                        click = False

            if(survivalModeButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, white, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, shopButton, 0, borderRadius)
                pygame.draw.rect(screen, black, optionsButton, 0, borderRadius)
                self.drawText("Story Mode",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Survival Mode",littleFont, black, screen, halfWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                self.drawText("Options",littleFont, white, screen, halfWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                if(click):
                    if(mouseLifted and survivalModeButton.collidepoint((storedX, storedY))):
                        print("Survival mode selected")
                        click = False
                    elif(mouseLifted):
                        click = False

            if(shopButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, white, shopButton, 0, borderRadius)
                pygame.draw.rect(screen, black, optionsButton, 0, borderRadius)
                self.drawText("Story Mode",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Survival Mode",littleFont, white, screen, halfWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, black, screen, fourthWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                self.drawText("Options",littleFont, white, screen, halfWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                if(click):
                    if(mouseLifted and shopButton.collidepoint((storedX, storedY))):
                        pygame.mixer.music.fadeout(fade)
                        ShopMenu.shopMenu(ShopMenu)
                        pygame.mixer.music.load('Assets\Sounds\MainMenu.wav')
                        pygame.mixer.music.play(loops=-1)
                        click = False
                    elif(mouseLifted):
                        click = False

            if(optionsButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, shopButton, 0, borderRadius)
                pygame.draw.rect(screen, white, optionsButton, 0, borderRadius)
                self.drawText("Story Mode",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Survival Mode",littleFont, white, screen, halfWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                self.drawText("Options",littleFont, black, screen, halfWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)       
                if(click):
                    if(mouseLifted and optionsButton.collidepoint((storedX, storedY))):
                        print("Options menu selected")
                        click = False
                    elif(mouseLifted):
                        click = False
                    

            if(not shopButton.collidepoint((mx, my)) and not storyModeButton.collidepoint((mx, my)) 
            and not survivalModeButton.collidepoint((mx, my)) and not optionsButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, storyModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, survivalModeButton, 0, borderRadius)
                pygame.draw.rect(screen, black, shopButton, 0, borderRadius)
                pygame.draw.rect(screen, black, optionsButton, 0, borderRadius)
                self.drawText("Story Mode",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Survival Mode",littleFont, white, screen, halfWindowWidth+buttonWidth/2, firstButtonHeight+buttonHeight/2)
                self.drawText("Shop",littleFont, white, screen, fourthWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)
                self.drawText("Options",littleFont, white, screen, halfWindowWidth+buttonWidth/2, secondButtonHeight+buttonHeight/2)


            mouseLifted = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True
                        storedX, storedY = pygame.mouse.get_pos()
                if(event.type == MOUSEBUTTONUP):
                    if(event.button == 1):
                        mouseLifted = True

            pygame.display.update()