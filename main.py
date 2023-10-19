import pygame
from sys import exit
from random import randint

def display_score():
    curr_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = game_font.render(f'{curr_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (200, 50))
    screen.blit(score_surface, score_rect)
    # print(curr_time)
    return curr_time

def obstacle_movement(obs_list):
    if obs_list:
        for obs_rect in obs_list:
            obs_rect.x -= 5
            
            if obs_rect.bottom == background_surface.get_height():
                screen.blit(snail_surface, obs_rect)
            else: 
                screen.blit(fly_surface, obs_rect)
                    
        obs_list = [obs for obs in obs_list if obs.x > -100]
        
        return obs_list
    else: 
        return []

def collision_check(player, obs):
    if obs:
        for obs_rect in obs:
            if player.colliderect(obs_rect):
                return False
    return True

def player_animation():
    global player_surface, player_index
    
    # Jump animation
    if player_rect.bottom < background_surface.get_height():
        player_surface = player_jump
    else:
        # Walking animation on floor
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
            
        player_surface = player_walk[int(player_index)]

pygame.init()

# Game variable
game_active = False
start_time = 0
score = 0

# Screen dimensions / variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')

#Clock
clock = pygame.time.Clock()

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation, 500)

fly_animation = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation, 300)

# Font
game_font = pygame.font.Font('RunnerGame/font/Pixeltype.ttf', 50)

# Background surfaces
background_surface = pygame.image.load('RunnerGame/graphics/Sky.png').convert()
foreground_surface = pygame.image.load('RunnerGame/graphics/ground.png').convert()

# Score surface
score_surface = game_font.render('Score: ', False, 'Black')
score_rect = score_surface.get_rect(center = (100, 50))

# Obstacles
obstacle_rect_list = []

snail_x_pos = 900
snail_frame_1 = pygame.image.load('RunnerGame/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('RunnerGame/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('RunnerGame/graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('RunnerGame/graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

# Player
player_walk1 = pygame.image.load('RunnerGame/graphics/Player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('RunnerGame/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load('RunnerGame/graphics/Player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, background_surface.get_height()))

# Player Gravity
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('RunnerGame/graphics/Player/player_stand.png').convert_alpha()
player_stand= pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = game_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = game_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

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
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if game_active:        
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), background_surface.get_height())))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), background_surface.get_height() - 90)))
            
            if event.type == snail_animation:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
            
    if game_active:
        # Updates
        screen.blit(background_surface, (0, 0))
        screen.blit(foreground_surface, (0, background_surface.get_height()))
        screen.blit(score_surface, score_rect)
        
        score = display_score()
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom >= background_surface.get_height():
            player_rect.bottom = background_surface.get_height()
        
        player_animation()
        screen.blit(player_surface, player_rect)
        
        # Obstacles movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        # Collision
        game_active = collision_check(player_rect, obstacle_rect_list)
        
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, background_surface.get_height())
        player_gravity = 0
        
        score_message = game_font.render(f'Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 320))
        
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        
    pygame.display.update()
    clock.tick(60)