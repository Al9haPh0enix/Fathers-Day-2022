import pygame
pygame.init()

width = 16
height = 16

pixels = [[True for y in range(height)] for x in range(width)]

with open("input.in", "r") as f:
    pixels = [[x=="1" for x in y.strip().split(" ")] for y in f.readlines()]

w = pygame.display.set_mode((400, 400))
c = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    w.fill((0, 0, 0))

    snapx = 400/width
    snapy = 400/height
    
    for x in range(width):
        for y in range(height):
            if pixels[x][y]:
                c = (255, 255, 255)
            else:
                c = (0, 0, 0)
            pygame.draw.rect(w, c, pygame.Rect(x*snapx, y*snapy, snapx, snapy))
            if y != 0:
                pygame.draw.line(w, (127, 127, 127), (x*snapx, y*snapy), ((x*snapx)+snapx, y*snapy), 1)
            if x != 0:
                pygame.draw.line(w, (127, 127, 127), (x*snapx, y*snapy), ((x*snapx), (y*snapy)+snapy), 1)
    
    pygame.display.flip()
