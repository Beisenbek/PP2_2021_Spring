import pygame
import os

my_images = {}

def get_image(path):
        global my_images
        image = my_images.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                print(canonicalized_path)
                image = pygame.image.load(canonicalized_path)
                my_images[path] = image
        return image

def get_image2(path):
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        print(canonicalized_path)
        image = pygame.image.load(canonicalized_path)
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
       
        screen.fill((255, 255, 255))


        screen.blit(get_image2('images/ball.png'),(20, 20))

        
        pygame.display.flip()


