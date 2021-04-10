import pygame 
import time
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255,255,102)
green = (0,255,0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption("Snake game")

snake_block = 10
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("papyrusttc", 50)
score_font = pygame.font.SysFont("ヒラキノ角コシックw0ttc", 35)

def display_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

def draw_snake(snake_block, snake_list):
    for item in snake_list:
        pygame.draw.rect(dis, black, [item[0], item[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height / 2
    
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    
    while not game_close:

        while game_over == True:
            dis.fill(blue)
            message("game over!", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) 

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)

        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        draw_snake(snake_block, snake_list)

        display_score(snake_length - 1)
   

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)
            
    pygame.quit()
    quit()

gameLoop()