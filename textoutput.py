import pygame  
from constants import * 
from player import *

initial_life = 5
initial_score = 0

def end_screen(screen, score, my_font, life):
    screen.fill((0, 0, 0))
    end_score_text_surface = my_font.render(f'Your score was: {score}', False, (255, 255, 255))
    end_text_continue_surface = my_font.render(f'To continue click r', False, (255, 255, 255))
    end_text_quit_surface = my_font.render(f'To quit click ESC', False, (255, 255, 255))
    screen.blit(end_score_text_surface, (550,280))
    screen.blit(end_text_continue_surface, (550,320))
    screen.blit(end_text_quit_surface, (550, 360))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit()
    if keys[pygame.K_r]:
        return restart_game()



def scoreboard(screen, score, my_font, life):
    score_text_surface = my_font.render(f'Score: {score}', False, (255, 255, 255))
    life_text_surface = my_font.render(f'Lives: {life}', False, (255, 255, 255))
    screen.blit(score_text_surface, (1180,10))
    screen.blit(life_text_surface, (1180,30))

def restart_game():
    life = initial_life
    score = initial_score
    return life, score