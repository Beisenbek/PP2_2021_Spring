import pygame 

pygame.init()

BLUE = (0, 0, 255)
width = 500
height = 500

screen = pygame.display.set_mode((width, height))

isPressed = False
prevPoint = (0, 0)
curPoint = (0, 0)

#0 - pencil, 1 - rectangle
currentTool = 0
toolCount = 2

def drawRectangle(surface, x,y, w, h):
    pygame.draw.rect(surface, BLUE, [x, y, w, h],5)

def drawCircle(surface, x,y):
    pygame.draw.circle(surface, BLUE, (x, y), 5)

def drawLine(surface, startPos, endPos):
    pygame.draw.line(surface, BLUE, startPos, endPos, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                currentTool = (currentTool + 1) % toolCount
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPoint = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
            
    if currentTool == 0:
        drawLine(screen, prevPoint, curPoint)
    elif currentTool == 1:
        drawRectangle(screen, 40,40,100,100)

    pygame.display.flip()