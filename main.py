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

# Score surface
score_surface = score_font.render('Score: ', False, 'Black')
score_rect = score_surface.get_rect(center = (100, 50))

# Enemies
snail_surface = pygame.image.load('RunnerGame/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 900
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, background_surface.get_height()))

# Player
player_surface = pygame.image.load('RunnerGame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, background_surface.get_height()))

while True:
    # Exit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')

    # Updates
    screen.blit(background_surface, (0, 0))
    screen.blit(foreground_surface, (0, background_surface.get_height()))
    pygame.draw.rect(screen, 'White', score_rect)
    pygame.draw.rect(screen, 'White', score_rect, 10)
    screen.blit(score_surface, score_rect)
    
    # Snail movement
    snail_rect.x -= 5
    if (snail_rect.right < -50):
        snail_rect.left = snail_x_pos
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    
    # player_rect.colliderect(snail_rect)
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
    
    pygame.display.update()
    clock.tick(60)