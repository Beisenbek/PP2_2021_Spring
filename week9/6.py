import pygame
import os

def get_image(path):
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        print(canonicalized_path)
        image = pygame.image.load(canonicalized_path)
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

loaded_image = get_image('images/ball.png')

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
       
        screen.fill((255, 255, 255))


        screen.blit(loaded_image,(20, 20))
        screen.blit(loaded_image,(50, 120))

        
        pygame.display.flip()


