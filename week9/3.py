import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

is_blue = True
color = (0, 0, 255)
x = 30
y = 30
step = 3
#1/60
fps = 60

clock = pygame.time.Clock()


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue

        if(not is_blue): color = (255, 0, 0)
        else: color = (0, 0, 255)

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: y -= step
        if pressed[pygame.K_DOWN]: y += step
        if pressed[pygame.K_LEFT]: x -= step
        if pressed[pygame.K_RIGHT]: x += step 
        
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        
        clock.tick(fps)

