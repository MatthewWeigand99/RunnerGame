import pygame
from sys import exit

pygame.init()

# Game variable
game_active = True

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

# Gravity
player_gravity = 0

while True:
    # Exit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            # Player jump w/ mouse button    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == background_surface.get_height():
                    player_gravity = -20
                    
            # Player jump w/ space button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == background_surface.get_height():
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = snail_x_pos
                game_active = True
            
    if game_active:
        # Updates
        screen.blit(background_surface, (0, 0))
        screen.blit(foreground_surface, (0, background_surface.get_height()))
        # pygame.draw.rect(screen, 'White', score_rect)
        # pygame.draw.rect(screen, 'White', score_rect, 10)
        screen.blit(score_surface, score_rect)
        
        # Snail movement
        snail_rect.x -= 5
        if (snail_rect.right < -50):
            snail_rect.left = snail_x_pos
        screen.blit(snail_surface, snail_rect)
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom >= background_surface.get_height():
            player_rect.bottom = background_surface.get_height()
            
        screen.blit(player_surface, player_rect)
        
        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
        
    pygame.display.update()
    clock.tick(60)