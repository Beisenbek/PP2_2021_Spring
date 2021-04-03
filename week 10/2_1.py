import pygame
import math
import time

def create_background(width, height):
        colors = [(255, 255, 255), (0, 0, 255)]
        background = pygame.Surface((width, height))
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(
                                background, 
                                colors[(row + col) % 2],
                                pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width
        return background



def run_demos(width, height, fps):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('press space to see next demo')
        background = create_background(width, height)
        clock = pygame.time.Clock()

        
        while True:
                screen.blit(background, (0, 0))
                pygame.display.flip()
                clock.tick(fps)

run_demos(400,400,60)