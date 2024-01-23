import pygame
from fun_menu import menu
def leaderboard(player_data, screen, clock, window_width, window_height):
    from fun_game_loop import game_loop
    pygame.init()

    running = True
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 24)

    while running:
        screen.fill((153, 191, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(pygame.mouse.get_pos()):
                    reset_game(screen, clock, window_width, window_height)

        font2 = pygame.font.Font(None, 32)
        text2 = f"{player_data['name']},   Twój wynik to:    {player_data['time']} sekund!"
        text2_surface = font2.render(text2, True, (255, 255, 255))
        screen.blit(text2_surface, (WIDTH // 2 - text2_surface.get_width() // 2, 50))

        filename = 'gracze.txt'
        scores_dict = read_scores_from_file(filename)
        sorted_dict = sort_dict(scores_dict)
        top_10_scores = list(sorted_dict.items())[:10] #lista

        font3 = pygame.font.Font(None, 32)
        text3 = "TOP 10  WYNIKÓW:"
        text3_surface = font3.render(text3, True, (255, 255, 255))
        screen.blit(text3_surface, (WIDTH // 2 - text3_surface.get_width() // 2, 140))
        text_y = 180
        place = 1
        for player, time in top_10_scores:
            text_surface_place = font.render(f"{place}.    ", True, (255, 255, 255))
            text_surface = font.render(f"Gracz:    {player}      ({time}s)", True, (255, 255, 255))
            screen.blit(text_surface, (310, text_y))
            screen.blit(text_surface_place, (280, text_y))

            place += 1
            text_y += text_surface.get_height() + 10

        play_again_button = draw_play_again_button(screen, window_width=800, window_height=600)
        pygame.display.update()

    pygame.quit()


def reset_game(screen, clock, window_width, window_height):
    from fun_game_loop import game_loop
    player_data = menu(screen, clock, window_width, window_height)
    game_loop(screen, clock, window_width, window_height, player_data)

def read_scores_from_file(filename):
    scores = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) >= 2:
                name = parts[0]
                time_str = parts[1]
                time = float(time_str)
                scores[name] = time
    return scores

def sort_dict(scores_dict):
    items = list(scores_dict.items()) #tworzy tuple
    n = len(items)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    sorted_dict = dict(items) #tworzy słownik
    return sorted_dict
def draw_play_again_button(screen, window_width, window_height):
    font = pygame.font.Font(None, 36)
    button_text = font.render("zagraj jeszcze raz", True, (116, 186, 242))
    button_rect = button_text.get_rect(center=(window_width // 2 - 10, window_height // 2 + 200))
    button_rect.width = 240
    button_rect.height = 60
    pygame.draw.rect(screen, (255, 255, 255), button_rect)
    pygame.draw.rect(screen, (116, 186, 242), button_rect, 3)
    text_width, text_height = button_text.get_size()
    text_x = button_rect.x + (button_rect.width - text_width) // 2
    text_y = button_rect.y + (button_rect.height - text_height) // 2
    screen.blit(button_text, (text_x, text_y))

    return button_rect