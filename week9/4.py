import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

image = pygame.image.load('images/ball.png')


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
       
        screen.fill((255, 255, 255))


        screen.blit(image,(20, 20))

        
        pygame.display.flip()


