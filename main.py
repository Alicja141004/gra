import pygame
from fun_game_loop import game_loop
from fun_menu import menu

pygame.init()
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

player_data = menu(screen, clock, window_width, window_height)
if player_data['name']:
    game_loop(screen, clock, window_width, window_height, player_data)
