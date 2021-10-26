from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame
import sys
from Models.GameObjects.Character import Character
import random
from Models.GameObjects.Enemy import Enemy
from Models.GameObjects.Projectile import Projectile
import pickle
from Models.GameSounds import GameSounds
from UI.GameMenu.PauseLoop import PauseLoop
import json
import time

from UI.GameMenu.RoundCompletionPage import RoundCompletionPage
from UI.GameMenu.RoundNotCompletedPage import RoundNotCompletedPage

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
        barY = 88
 
        pygame.draw.rect(screen, grey, pygame.Rect(barX, WINDOW_HEIGHT - barY, 104, 8), 3)
        pygame.draw.rect(screen, color,pygame.Rect(barX+2, WINDOW_HEIGHT - barY+2, playerShield/4, 4))

    def drawPlayerHealth(character, health):
        barX = 50
        barY = 100

        pygame.draw.rect(screen, grey, pygame.Rect(barX, WINDOW_HEIGHT - barY, 104, 8), 3)
        pygame.draw.rect(screen, red, pygame.Rect(barX+2, WINDOW_HEIGHT - barY+2, health, 4))

    def drawEnemyHealth(enemy):
        barX = enemy.x + enemy.healthBarOffsetX
        barY = enemy.y + enemy.healthBarOffsetY

        pygame.draw.rect(screen, grey, pygame.Rect(barX, barY, 104, 8), 3)
        pygame.draw.rect(screen, red, pygame.Rect(barX+2, barY+2, enemy.health, 4))  

    

    def play(self, screen):

        #TODO: Still need to add the different projectiles or shot styles that the player bought
        try:
            with open('SaveData.p', 'rb') as handle:
                b = pickle.load(handle)
            level = b['level']
            characterName = b['characterPath']
            gems = b['gems']
            originalHealth = b['health']
            health = b['health']
            handle.close()
        except:
            dictobj = {'level': 1, 'characterPath': "Sword Of Storms", 'gems': 0, 'health': 100}
            filename = "SaveData.p"
            fileobj = open(filename, 'wb')
            pickle.dump(dictobj, fileobj)
            fileobj.close()
            level = dictobj['level']
            characterName = dictobj['characterPath']
            gems = dictobj['gems']
            originalHealth = dictobj['health']
            health = dictobj['health']

        jsonToRead = "level"+str(level)
        with open("Models\\Levels\\"+jsonToRead+".json", 'r+') as f:
            levelData = json.load(f)
        level = levelData['level']
        gemsEarnedPerKill = levelData['gemsPerKill']
        enemies = levelData['round']['enemies']
        enemyPaths = []
        enemyAmount = levelData['round']['totalAmount']
        enemyAmountDictionary = {}
        enemyAmountOnScreen = levelData['round']['amountOnScreen']
        for enemy in enemies:
            enemyPaths.append(enemies[enemy]['path'])
            enemyAmountDictionary[enemies[enemy]['path']] = enemies[enemy]['amount']
            

        waiting = False
        roundComplete = False
        enemiesKilled = 0
        enemyList = []
        enemyWaitingList = []
        for x in range(0, enemyAmount):
            enemyY = random.randint(WINDOW_HEIGHT/2 + 50, WINDOW_HEIGHT-60)
            added = False
            while not added:
                enemyPath = random.randint(0, len(enemyPaths) - 1)
                if enemyAmountDictionary[enemyPaths[enemyPath]] >= 1:
                    enemyAmountDictionary[enemyPaths[enemyPath]] -= 1
                    added = True
            
            enemyFileName = enemyPaths[enemyPath] + "\walk.png"
            enemy = Enemy(WINDOW_WIDTH, enemyY, enemyFileName)
            enemyWaitingList.append(enemy)
        
        buffer = False
        running = True
        click = False
        mouseLifted = False
        bg = pygame.image.load("Assets/BG_PalmTree/marsh.jpg")
        picture = pygame.transform.scale(bg, (1000, 600))
        white = (255, 255, 255)
        black = (0, 0, 0)
        blue = (0, 0, 255)
        littleFont = pygame.font.SysFont(None, 28)
        pauseButtonHeight = 25
        pauseButtonWidth = 100
        pauseButtonYPos = 10
        pauseButtonXPos = WINDOW_WIDTH-110
        borderRadius = 5
        storedX, storedY = 0, 0

        characterFileName = "Assets\Characters\\"+ characterName+"\Idle.png"
        character = Character(characterName, characterFileName)
        character.setAnimationFileName(characterFileName)


        frame = 0
        characterFrame = 0
        attackMeter = 0
        increasing = True
        releasePoint = (110, WINDOW_HEIGHT - 140)
        projectileList = []

        clock = pygame.time.Clock()
        fps = 140

        fade = 1000
        sounds = GameSounds()
        pygame.mixer.init()
        battleSound = pygame.mixer.Sound(sounds.getRandomBattleSong())
        battleSound.set_volume(.5)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(sounds.getRandomBattleSong()))

        died = False
        fadeAlpha = 0
        fadeScreen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT)) 
        fadeScreen.fill(black)

        while running:
                

            #Player Died
            if health <= 0 and not roundComplete:
                died = True
                health = 0
                roundComplete = True
                

            #Player won
            if enemiesKilled == enemyAmount and not died:
                roundComplete = True
                running = False

                pygame.mixer.Channel(0).fadeout(fade + 1000)
                gameState = RoundCompletionPage.roundComplete(RoundCompletionPage)
                try:
                    level += 1

                    dict = {'level': level, 'characterPath': characterName, 'gems': gems, 'health': originalHealth}
                    filename = "SaveData.p"
                    file = open(filename, 'wb')
                    pickle.dump(dict, file)
                    file.close()
    
                except:
                    print("problem saving game data")
                if(gameState == 0):
                    ### Go to the next level screen for GameScreenPage
                    return True
                elif(gameState == 1):
                    ### Go back to the main menu
                    return False


            #Dont exceed enemy limit on screen
            if(len(enemyList) < enemyAmountOnScreen and len(enemyWaitingList) != 0 and not waiting):
                waiting = True
                enemyList.append(enemyWaitingList[0])
                enemyWaitingList.remove(enemyWaitingList[0])

            #Draw screen and character
            clock.tick(fps)
            screen.blit(picture, (0, 0))
            screen.blit(character.animationList[character.index], (32, WINDOW_HEIGHT - 180))
            self.drawText("Level: " + str(level), font, black, screen, 110, 30)

            color = (character.color['r'], character.color['g'], character.color['b'])
            self.drawAttackMeter(attackMeter, color)
            self.drawPlayerHealth(character, health)

            #manage attack meter
            if(character.attacking):
                if(attackMeter == 400):
                    increasing = False
                elif(attackMeter == 0):
                    increasing = True
                if(increasing):
                    attackMeter += 5
                elif(not increasing):
                    attackMeter -= 5
            
            #Increment enemy frame index and player health
            frame = frame + 5
            if frame >= 100 :
                waiting = False
                frame = 0
                for enemy in enemyList:
                    enemy.index += 1
                    if enemy.index >= len(enemy.animationList):
                        if enemy.selfDestruct == 1 and enemy.attacking:
                            enemyList.remove(enemy)
                        enemy.index = 0
                        
                        
                    if enemy.index == enemy.attackFrame and enemy.attacking:
                        health -= enemy.damage
                        
            
            #Update character frames
            characterFrame = characterFrame + (1 * character.converter.speed)
            if(characterFrame >= 100):
                character.index += 1
                characterFrame = 0
                if(character.index >= len(character.animationList) and not character.attacking and not character.releasing):
                    character.index = 0
                elif(character.index >= character.getHoldFrame() and character.attacking):
                    character.index = character.index - 1
                elif(character.releasing):
                    if(character.index >= len(character.animationList)):
                        character.releasing = False
                        character.index = 0
                        characterFileName = "Assets\Characters\\" + characterName + "\Idle.png"
                        character.setAnimationFileName(characterFileName)

            #Projectile hit detection
            for projectile in projectileList:
                for enemy in enemyList:
                    if enemy.hitBy((projectile.x, projectile.y), projectile.width, projectile.height):
                        try:
                            hitSound = pygame.mixer.Sound('Assets\Sounds\Effects\hit.wav')
                            hitSound.set_volume(3.0)
                            pygame.mixer.Channel(2).play(hitSound)
                            enemy.takeDamage(projectile.power * enemy.multiplyer)
                            projectileList.remove(projectile)
                            if enemy.health < 0:
                                enemyList.remove(enemy)
                                enemiesKilled += 1
                                gems += gemsEarnedPerKill
                        except:
                            print("trying to access projectile that was removed")

                try:
                    if(projectile.x > WINDOW_WIDTH or projectile.y > WINDOW_HEIGHT):
                        projectileList.remove(projectile)
                    projectile.projectilePath(screen)
                except:
                    print("trouble deleting the projectile off screen")

            #Drawing enemies on screen
            for enemy in enemyList:
                self.drawEnemyHealth(enemy)
                enemy.checkPosition()
                enemy.updatePosition()
                screen.blit(enemy.animationList[enemy.index], (enemy.x, enemy.y))
                # Draws the hitbox: pygame.draw.rect(screen, grey, pygame.Rect(enemy.x+enemy.hitboxOffsetX, enemy.y + enemy.hitboxOffsetY, enemy.w, enemy.h), 2)

            mx, my = pygame.mouse.get_pos()
            pauseButton = pygame.Rect(pauseButtonXPos, pauseButtonYPos, pauseButtonWidth, pauseButtonHeight)

            #Pause button
            if(pauseButton.collidepoint((mx, my))):
                pygame.draw.rect(screen, white, pauseButton, 0, borderRadius)

                self.drawText("Pause", littleFont, black, screen, pauseButtonXPos+pauseButtonWidth/2, pauseButtonYPos+pauseButtonHeight/2)

                if(click):
                    if(mouseLifted and pauseButton.collidepoint((storedX, storedY))):
                        pygame.mixer.Channel(0).fadeout(fade)
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

            #Draw fading screen
            if died:
                fadeAlpha += 1
                fadeScreen.set_alpha(fadeAlpha)
                screen.blit(fadeScreen, (0, 0))

            #Start sound fading
            if fadeAlpha == 1:
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('Assets\Sounds\Effects\death.wav'))
                pygame.mixer.Channel(0).fadeout(fade)
                
            #Screen transition to post round screen
            if fadeAlpha == 300:
                time.sleep(.62)
                gameState = RoundNotCompletedPage.roundFailed(RoundNotCompletedPage, enemiesKilled)

                try:
                    dict = {'level': level, 'characterPath': characterName, 'gems': gems, 'health': originalHealth}
                    filename = "SaveData.p"
                    file = open(filename, 'wb')
                    pickle.dump(dict, file)
                    file.close()
                except:
                    print("problem saving game data")
                if(gameState == 0):
                    ### Go to the next level screen for GameScreenPage
                    return True
                elif(gameState == 1):
                    ### Go back to the main menu
                    return False    


            #Handle input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        enemyY = random.randint(WINDOW_HEIGHT/2 + 50, WINDOW_HEIGHT-60)
                        enemyFileName = "Assets\Enemies\Stormhead\walk.png"
                        enemy = Enemy(WINDOW_WIDTH, enemyY, enemyFileName)
                        enemyList.append(enemy)
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and not character.attacking and not died:
                        storedX, storedY = pygame.mouse.get_pos()
                        click = True
                        buffer = True
                        if not pauseButton.collidepoint((mx, my)):
                            character.attacking = True
                            character.releasing = False
                            character.index = 0
                            characterFileName = "Assets\Characters\\" + characterName + "\Attack.png"
                            character.setAnimationFileName(characterFileName)
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1 and not died:
                        mouseLifted = True
                        character.attacking = False
                        character.releasing = True
                        character.index = character.getHoldFrame()
                        mousePos = pygame.mouse.get_pos()
                        if len(projectileList) <= 10:
                            newProjectile = Projectile("1.png", character.projectileColor, releasePoint, mousePos, attackMeter/4)
                            newProjectile.findAngle()
                            projectileList.append(newProjectile)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Assets\\Sounds\\Effects\\attack.wav'))
                        attackMeter = 0

            pygame.display.update()