import pygame, sys
def menu(screen, clock, window_width, window_height):
    running = True
    player_data = {'name': "", 'time': 0}
    input_active = False
    input_rect = pygame.Rect(window_width // 2 - 100, window_height // 2 - 50, 200, 50)

    while running:
        screen.fill((153, 191, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                if window_width // 2 - 50 <= x <= window_width // 2 + 50 and window_height // 2 + 25 <= y <= window_height // 2 + 75:
                    player_data['name'] = player_data['name'].strip()
                    if player_data['name']:
                        return player_data

                if window_width // 2 - 50 <= x <= window_width // 2 + 50 and window_height // 2 + 125 <= y <= window_height // 2 + 175:
                    pygame.quit()
                    sys.exit()

                if input_rect.collidepoint(pos):
                    input_active = not input_active
                else:
                    input_active = False

            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        player_data['name'] = player_data['name'][:-1]
                    elif event.key == pygame.K_RETURN:
                        player_data['name'] = player_data['name'].strip()
                        if player_data['name']:
                            return player_data
                    else:
                        player_data['name'] += event.unicode

        font = pygame.font.Font(None, 36)
        tytul_font = pygame.font.Font(None, 72)
        tytul_text = tytul_font.render("Narciarz", True, (255, 255, 255))
        start_text = font.render("START", True, (255, 255, 255))
        exit_text = font.render("EXIT", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(window_width // 2, window_height // 2 + 50))
        exit_rect = exit_text.get_rect(center=(window_width // 2, window_height // 2 + 150))

        screen.blit(tytul_text, (window_width // 2 - tytul_text.get_width() // 2, 50))
        screen.blit(start_text, start_rect)
        screen.blit(exit_text, exit_rect)

        pygame.draw.rect(screen, (255, 255, 255), input_rect, 2)

        if input_active:
            pygame.draw.rect(screen, ((182, 236, 250)), input_rect)

        input_text = font.render(player_data['name'], True, (255, 255, 255))
        screen.blit(input_text, input_rect.move(15, 15))

        pygame.display.update()
        clock.tick(60)
    player_data = game_loop(screen, clock, window_width, window_height, player_data)
    leaderboard(player_data, screen, clock, window_width, window_height)

    return player_data