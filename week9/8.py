import pygame



pygame.init()
screen = pygame.display.set_mode((400, 300))
screen.fill((0, 0, 255))
done = False

surface = pygame.Surface((100, 100),pygame.SRCALPHA)
surface.fill((255,255,255))

surface2 = pygame.Surface((200, 200),pygame.SRCALPHA)
surface2.fill((255,0,0))
surface2.set_alpha(120)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

        screen.blit(surface,(30, 30))
        screen.blit(surface2,(50, 40))
        
        pygame.display.flip()


