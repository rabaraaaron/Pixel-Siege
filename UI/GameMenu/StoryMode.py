from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame
import sys
from Models.Characters.Character import Character

from UI.GameMenu.PauseLoop import PauseLoop

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 75)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
grey = (105, 105, 105)



class StoryMode:

    def drawText(text, font, color, surface, x, y):
            textObject = font.render(text, 1, color)
            textRec = textObject.get_rect()
            textRec.center = (x, y)
            surface.blit(textObject, textRec)

    def drawAttackMeter(playerShield):
        if playerShield > 400:
            playerShieldColor = green
            playerShield = 400
        elif playerShield > 300:
            playerShieldColor = green
        elif playerShield > 150:
            playerShieldColor = yellow
        else:
            playerShieldColor= red
 
        pygame.draw.rect(screen, grey, pygame.Rect(50, WINDOW_HEIGHT - 100, 104, 8), 3)
        pygame.draw.rect(screen, (0, 255, 0),pygame.Rect(52, WINDOW_HEIGHT - 98, playerShield/4, 4))
        print(playerShield)

    
    def play(self, screen):
        
        running = True
        click = False
        mouseLifted = False
        bg = pygame.image.load("Assets/BG_PalmTree/marsh.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        white = (255, 255, 255)
        black = (0, 0, 0)
        littleFont = pygame.font.SysFont(None, 28)
        pauseButtonHeight = 25
        pauseButtonWidth = 100
        pauseButtonYPos = 10
        pauseButtonXPos = WINDOW_WIDTH-110
        borderRadius = 5
        storedX, storedY = 0, 0
        fileName = "Assets\SciFi\Mage Samurai\Idle.png"
        character = Character("mage samurai", fileName)
        character.setAnimationFileName(fileName)
        attackHold = character.holdFrame
        attacking = False
        releasing = False
        index = 0
        clock = pygame.time.Clock()
        frame = 0
        attackMeter = 0
        increasing = True


        while(running):
            screen.blit(picture, (0, 0))
            screen.blit(character.animationList[index], (32, WINDOW_HEIGHT - 180))

            self.drawAttackMeter(attackMeter)
            if(attacking):
                if(attackMeter == 400):
                    increasing = False
                elif(attackMeter == 0):
                    increasing = True
                if(increasing):
                    attackMeter += 1
                elif(not increasing):
                    attackMeter -= 1
            


            frame = frame+1
            if(frame == 100):
                frame = 0
                index = index + 1
                if(index >= len(character.animationList) and not attacking and not releasing):
                    index = 0
                elif(index >= attackHold and attacking):
                    index = index - 1
                elif(releasing):
                    if(index >= len(character.animationList)):
                        releasing = False
                        index = 0
                        fileName = "Assets\SciFi\Mage Samurai\Idle.png"
                        character.setAnimationFileName(fileName)



            
            mx, my = pygame.mouse.get_pos()
            pauseButton = pygame.Rect(pauseButtonXPos, pauseButtonYPos, pauseButtonWidth, pauseButtonHeight)

            if(pauseButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, pauseButton, 0, borderRadius)

                self.drawText("Pause", littleFont, black, screen, pauseButtonXPos+pauseButtonWidth/2, pauseButtonYPos+pauseButtonHeight/2)

                if(click):
                    if(mouseLifted and pauseButton.collidepoint((storedX, storedY))):
                        gameState = PauseLoop.pauseLoop(PauseLoop, screen)
                        if(gameState == 0):
                            ### unpause the game
                            pass
                        elif(gameState == 1):
                            ### make the GameScreenPage run this page again due to restart code 1
                            return True
                        elif(gameState == 2):
                            ### this is code 2, which means to the menu!
                            return False
                        click = False
                    elif(mouseLifted):
                        click = False

            if(not pauseButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, black, pauseButton, 0, borderRadius)
                self.drawText("Pause", littleFont, white, screen, pauseButtonXPos+pauseButtonWidth/2, pauseButtonYPos+pauseButtonHeight/2)

            mouseLifted = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        frame = 0
                        storedX, storedY = pygame.mouse.get_pos()
                        click = True
                        attacking = True
                        releasing = False
                        index = 0
                        fileName = "Assets\SciFi\Mage Samurai\Slam attack.png"
                        character.setAnimationFileName(fileName)
                        animationList = character.animationList[:len(character.animationList)-len(character.animationList)-character.getHoldFrame()]
                    

                if(event.type == MOUSEBUTTONUP):
                    if(event.button == 1):
                        frame = 0
                        mouseLifted = True
                        attacking = False
                        releasing = True
                        index = 5
                        animationList = character.animationList[len(character.animationList)-len(character.animationList)-character.getHoldFrame():]
                        attackMeter = 0
                    
            pygame.display.update()








# from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP
# import pygame
# import sys
# from Models.SpriteSheetConverter import SpriteSheetConverter

# from UI.GameMenu.PauseLoop import PauseLoop

# pygame.init()

# WINDOW_HEIGHT = 600
# WINDOW_WIDTH = 1000

# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# font = pygame.font.SysFont(None, 75)
# red = (255, 0, 0)
# green = (0, 255, 0)
# yellow = (255, 255, 0)
# grey = (105, 105, 105)



# class StoryMode:

#     def drawText(text, font, color, surface, x, y):
#             textObject = font.render(text, 1, color)
#             textRec = textObject.get_rect()
#             textRec.center = (x, y)
#             surface.blit(textObject, textRec)

#     def drawAttackMeter(playerShield):
#         if playerShield > 400:
#             playerShieldColor = green
#             playerShield = 400
#         elif playerShield > 300:
#             playerShieldColor = green
#         elif playerShield > 150:
#             playerShieldColor = yellow
#         else:
#             playerShieldColor= red
 
#         pygame.draw.rect(screen, grey, pygame.Rect(50, WINDOW_HEIGHT - 100, 104, 8), 3)
#         pygame.draw.rect(screen, (0, 255, 0),pygame.Rect(52, WINDOW_HEIGHT - 98, playerShield/4, 4))
#         print(playerShield)

    
#     def play(self, screen):
        
#         running = True
#         click = False
#         mouseLifted = False
#         bg = pygame.image.load("Assets/BG_PalmTree/marsh.jpg")
#         picture = pygame.transform.scale(bg, (1000, 600))
#         white = (255, 255, 255)
#         black = (0, 0, 0)
#         littleFont = pygame.font.SysFont(None, 28)
#         pauseButtonHeight = 25
#         pauseButtonWidth = 100
#         pauseButtonYPos = 10
#         pauseButtonXPos = WINDOW_WIDTH-110
#         borderRadius = 5
#         storedX, storedY = 0, 0
#         fileName = "Assets\SciFi\Mage Samurai\Idle.png"
#         characterSpriteSheet = SpriteSheetConverter(fileName)
#         attackHold = characterSpriteSheet.getHoldFrame()
#         character1 = []
#         attacking = False
#         releasing = False
#         index = 0
#         clock = pygame.time.Clock()
#         frame = 0
#         attackMeter = 0
#         increasing = True

#         frameNames = characterSpriteSheet.getFrameNames()
#         for x in frameNames:
#             character1.append(characterSpriteSheet.parseSprite(x))

#         while(running):
#             screen.blit(picture, (0, 0))
#             screen.blit(character1[index], (32, WINDOW_HEIGHT - 180))

#             self.drawAttackMeter(attackMeter)
#             if(attacking):
#                 if(attackMeter == 400):
#                     increasing = False
#                 elif(attackMeter == 0):
#                     increasing = True
#                 if(increasing):
#                     attackMeter += 1
#                 elif(not increasing):
#                     attackMeter -= 1
            


#             frame = frame+1
#             if(frame == 100):
#                 frame = 0
#                 index = index + 1
#                 if(index >= len(character1) and not attacking and not releasing):
#                     index = 0
#                 elif(index >= attackHold and attacking):
#                     index = index - 1
#                 elif(releasing):
#                     if(index >= len(character1)):
#                         releasing = False
#                         index = 0
#                         fileName = "Assets\SciFi\Mage Samurai\Idle.png"
#                         characterSpriteSheet = SpriteSheetConverter(fileName)
#                         frameNames = characterSpriteSheet.getFrameNames()
#                         character1.clear()
#                         for x in frameNames:
#                             character1.append(characterSpriteSheet.parseSprite(x))


            
#             mx, my = pygame.mouse.get_pos()
#             pauseButton = pygame.Rect(pauseButtonXPos, pauseButtonYPos, pauseButtonWidth, pauseButtonHeight)

#             if(pauseButton.collidepoint((mx, my))):
#                 pygame.draw.rect(screen, white, pauseButton, 0, borderRadius)

#                 self.drawText("Pause", littleFont, black, screen, pauseButtonXPos+pauseButtonWidth/2, pauseButtonYPos+pauseButtonHeight/2)

#                 if(click):
#                     if(mouseLifted and pauseButton.collidepoint((storedX, storedY))):
#                         gameState = PauseLoop.pauseLoop(PauseLoop, screen)
#                         if(gameState == 0):
#                             ### unpause the game
#                             pass
#                         elif(gameState == 1):
#                             ### make the GameScreenPage run this page again due to restart code 1
#                             return True
#                         elif(gameState == 2):
#                             ### this is code 2, which means to the menu!
#                             return False
#                         click = False
#                     elif(mouseLifted):
#                         click = False

#             if(not pauseButton.collidepoint((mx, my))):
#                 pygame.draw.rect(screen, black, pauseButton, 0, borderRadius)
#                 self.drawText("Pause", littleFont, white, screen, pauseButtonXPos+pauseButtonWidth/2, pauseButtonYPos+pauseButtonHeight/2)

#             mouseLifted = False

#             for event in pygame.event.get():
#                 if(event.type == pygame.QUIT):
#                     sys.exit()
#                 if(event.type == MOUSEBUTTONDOWN):
#                     if(event.button == 1):
#                         frame = 0
#                         storedX, storedY = pygame.mouse.get_pos()
#                         click = True
#                         attacking = True
#                         releasing = False
#                         index = 0
#                         fileName = "Assets\SciFi\Mage Samurai\Slam attack.png"
#                         characterSpriteSheet = SpriteSheetConverter(fileName)
#                         frameNames = characterSpriteSheet.getFrameNames()
#                         character1.clear()
#                         frameSize = characterSpriteSheet.getFrameSize()
#                         for x in frameNames:
#                             character1.append(characterSpriteSheet.parseSprite(x))
#                         frameNames = frameNames[:len(frameNames)-len(frameNames)-attackHold]

#                 if(event.type == MOUSEBUTTONUP):
#                     if(event.button == 1):
#                         frame = 0
#                         mouseLifted = True
#                         attacking = False
#                         releasing = True
#                         index = 5
#                         frameNames = frameNames[len(frameNames)-len(frameNames)-attackHold:]
#                         attackMeter = 0
                    
#             pygame.display.update()