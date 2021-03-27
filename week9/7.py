import pygame
import os

my_images = {}

def get_image(path):
        global my_images
        print(my_images)
        print("===============")
        image = my_images.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                print(canonicalized_path)
                image = pygame.image.load(canonicalized_path)
                my_images[path] = image
        return image


pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

fps = 1000
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
       
        screen.fill((255, 255, 255))


        screen.blit(get_image('images/ball.png'),(20, 20))
        screen.blit(get_image('images/Enemy.png'),(120, 120))
        
        pygame.display.flip()
        clock.tick(fps)


