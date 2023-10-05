import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

score_font = pygame.font.Font('RunnerGame/font/Pixeltype.ttf', 50)


background_surface = pygame.image.load('RunnerGame/graphics/Sky.png')
foreground_surface = pygame.image.load('RunnerGame/graphics/ground.png')
text_surface = score_font.render('Score: ', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))
    screen.blit(foreground_surface, (0, background_surface.get_height()))
    screen.blit(text_surface, (25, 25))
    
    pygame.display.update()
    clock.tick(60)