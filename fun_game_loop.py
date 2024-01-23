import pygame
from fun_trees import generate_trees, drzewko, isCollision, zapisz_czas_zjazdu, check_and_reset_trees
from fun_leaderboard import leaderboard
def game_loop(screen, clock, window_width, window_height, player_data):
    pygame.init()
    start_time = pygame.time.get_ticks()
    direction = "RIGHT"
    icon = pygame.image.load("assets/skier (1).png")
    pygame.display.set_icon(icon)

    playerImgR = pygame.image.load("assets/skier.png")
    playerImgL = pygame.image.load("assets/skierleft.png")
    playerX = 368
    playerY = 20
    player_width = 64
    player_height = 64
    speedPlayer = 0

    drzewkoImg = pygame.image.load("assets/pine-tree (1).png")
    speedTree = 4
    tree_height = 64
    tree_width = 64

    trees = generate_trees(window_width, window_height, tree_width, tree_height)
    running = True

    while running:
        screen.fill((255, 255, 255))
        player_rect = pygame.Rect(playerX, playerY, player_width, player_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speedPlayer = -5
                    direction = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    speedPlayer = 5
                    direction = 'RIGHT'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    speedPlayer = 0

        playerX += speedPlayer

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        if direction == 'LEFT':
            pygame.draw.rect(screen, (255, 255, 255), (playerX, playerY, player_width, player_height))
            screen.blit(playerImgL, (playerX, playerY))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (playerX, playerY, player_width, player_height))
            screen.blit(playerImgR, (playerX, playerY))

        for tree in trees:
            treeX = tree['x']
            treeY = tree['y'] - tree_height

            tree_rect = pygame.Rect(tree['x'], tree['y'] - tree_height, tree_width, tree_height)
            drzewko(screen, drzewkoImg, tree_rect)
            tree['y'] -= speedTree

            if tree['y'] + tree_height < 0:
                check_and_reset_trees(trees, window_width, window_height, tree_width, tree_height)

            collision = isCollision(playerX, playerY, treeX, treeY, player_width, player_height, tree_width, tree_height)
            if collision:
                end_time = pygame.time.get_ticks()
                czas_zjazdu = (end_time - start_time) / 1000
                player_data['time'] = czas_zjazdu

                zapisz_czas_zjazdu("gracze.txt", player_data['name'], player_data['time'])
                leaderboard(player_data, screen, clock, window_width, window_height)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()