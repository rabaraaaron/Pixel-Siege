from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame
import sys
from Models.GameObjects.Character import Character
import math
from Models.GameObjects.Projectile import Projectile

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

    def drawAttackMeter(playerShield, color):
        barX = 50
        barY = 100
 
        pygame.draw.rect(screen, grey, pygame.Rect(barX, WINDOW_HEIGHT - barY, 104, 8), 3)
        pygame.draw.rect(screen, color,pygame.Rect(barX+2, WINDOW_HEIGHT - barY+2, playerShield/4, 4))

    def findAngle(releasePoint, mouse):
        try:
            angle = math.atan((releasePoint[1] - mouse[1]) / (releasePoint[0] - mouse[0]))
        except:
            angle = math.pi / 2

        if releasePoint[1] < mouse[1] and releasePoint[0] > mouse[0]:
            angle = abs(angle)
        elif releasePoint[1] < mouse[1] and releasePoint[0] < mouse[0]:
            angle = math.pi - angle
        elif releasePoint[1] > mouse[1] and releasePoint[0] < mouse[0]:
            angle = math.pi + abs(angle)
        elif releasePoint[1] > mouse[1] and releasePoint[0] > mouse[0]:
            angle = (math.pi * 2) - angle

        return angle


    
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
        releasePoint = (130, WINDOW_HEIGHT - 200)



        fileName = "Assets\SciFi\Mage Samurai\Idle.png"
        character = Character("mage samurai", fileName)
        character.setAnimationFileName(fileName)
        attackHold = character.holdFrame
        
        frame = 0
        attackMeter = 0
        increasing = True
        projectileList = []


        h = 0
        while(running):
            h += 1
            print(h)
            screen.blit(picture, (0, 0))
            screen.blit(character.animationList[character.index], (32, WINDOW_HEIGHT - 180))

            mouse = pygame.mouse.get_pos()
            rise = -(mouse[1] - releasePoint[1])
            run = mouse[0] - releasePoint[0]

            if(run != 0):
                slope = rise/run
                line = [releasePoint, slope]
            

            color = (character.color['r'], character.color['g'], character.color['b'])
            self.drawAttackMeter(attackMeter, color)
            if(character.attacking):
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
                character.index = character.index + 1
                if(character.index >= len(character.animationList) and not character.attacking and not character.releasing):
                    character.index = 0
                elif(character.index >= attackHold and character.attacking):
                    character.index = character.index - 1
                elif(character.releasing):


                    if(character.index >= len(character.animationList)):
                        character.releasing = False
                        character.index = 0
                        fileName = "Assets\SciFi\Mage Samurai\Idle.png"
                        character.setAnimationFileName(fileName)


            for projectile in projectileList:
                if(projectile.x > WINDOW_WIDTH):
                    projectileList.remove(projectile)
                projectile.draw(screen)
            
            # print(len(projectileList))


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
                        if(not pauseButton.collidepoint((mx, my))):
                            character.attacking = True
                            character.releasing = False
                            character.index = 0
                            fileName = "Assets\SciFi\Mage Samurai\Slam attack.png"
                            character.setAnimationFileName(fileName)
                            character.animationList = character.animationList[:len(character.animationList)-len(character.animationList)-character.getHoldFrame()]
                if(event.type == MOUSEBUTTONUP):
                    if(event.button == 1):
                        frame = 0
                        mouseLifted = True
                        character.attacking = False
                        character.releasing = True
                        character.index = character.getHoldFrame()
                        attackMeter = 0
                        projectileList.append(Projectile("08.png", releasePoint))

                    
            pygame.display.update()