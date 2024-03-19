import pygame, sys

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900, 900), 0, 32)
display = pygame.Surface((300, 300))

#grass
grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
print(map_data)
f.close()

while True:
    display.fill((0, 0, 0))

    #returns index as y and actual data as row
    for y, row in enumerate(map_data):
        #returns index of char as x and actual value until tiles run out
        for x, tile in enumerate(row):
            if tile:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.exit()
                sys.exit()
    
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()