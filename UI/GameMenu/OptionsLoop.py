import sys
import pygame
from pygame.constants import MOUSEBUTTONDOWN


WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

class OptionsLoop:

    def pauseLoop(screen):

        paused = True
        click = False

        while(paused):

            unpauseButton = pygame.Rect(WINDOW_WIDTH - 100, 10, 80, 20)
            restartButton = pygame.Rect(WINDOW_WIDTH - 100, 40, 80, 20)
            toMenuButton = pygame.Rect(WINDOW_WIDTH - 100, 70, 80, 20)

            mx, my = pygame.mouse.get_pos()

            if(unpauseButton.collidepoint((mx, my))):
                if(click):
                    return True

            if(restartButton.collidepoint((mx, my))):
                if(click):
                    return True

            if(toMenuButton.collidepoint((mx, my))):
                if(click):
                    return False

            pygame.draw.rect(screen, (0, 0, 0), unpauseButton)
            pygame.draw.rect(screen, (0, 0, 0), restartButton)
            pygame.draw.rect(screen, (0, 0, 0), toMenuButton)

            click = False

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    sys.exit()
                if(event.type == MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        click = True

            pygame.display.update()