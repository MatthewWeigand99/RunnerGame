import pygame
from sys import exit

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')

#Clock
clock = pygame.time.Clock()

# Font
score_font = pygame.font.Font('RunnerGame/font/Pixeltype.ttf', 50)

# Background surfaces
background_surface = pygame.image.load('RunnerGame/graphics/Sky.png').convert()
foreground_surface = pygame.image.load('RunnerGame/graphics/ground.png').convert()
text_surface = score_font.render('Score: ', False, 'Black')

# Enemies
snail_surface = pygame.image.load('RunnerGame/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 800


while True:
    # Exit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Updates
    screen.blit(background_surface, (0, 0))
    screen.blit(foreground_surface, (0, background_surface.get_height()))
    screen.blit(text_surface, (25, 25))
    
    # Snail movement
    snail_x_pos -= 5
    if (snail_x_pos < -50):
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 
                                background_surface.get_height() - 
                                snail_surface.get_height()))
    
    pygame.display.update()
    clock.tick(60)