import pygame, random, math
def drzewko(screen, drzewkoImg, tree_rect):
    screen.blit(drzewkoImg, tree_rect)

def isCollision(playerX, playerY, treeX, treeY, player_width, player_height, tree_width, tree_height):
    player_center_x = playerX + player_width / 2
    player_center_y = playerY + player_height / 2
    tree_center_x = treeX + tree_width / 2
    tree_center_y = treeY + tree_height / 2
    distance = math.sqrt((player_center_x - tree_center_x) ** 2 + (player_center_y - tree_center_y) ** 2)
    min_distance = 36
    if distance <= min_distance:
        return True
    return False

def generate_trees(window_width, window_height, tree_width, tree_height):
    return [{'x': random.randint(0, window_width - tree_width), 'y': random.randint(window_height, window_height * 2)}
            for _ in range(12)]

def check_and_reset_trees(trees, window_width, window_height, tree_width, tree_height):
    for tree in trees:
        if tree['y'] + tree_height < 0:
            tree['y'] = window_height
            tree['x'] = random.randint(0, window_width - tree_width)

def zapisz_czas_zjazdu(plik, imie, czas_zjazdu):
    with open(plik, 'a') as file:
        file.write(f"{imie}, {czas_zjazdu}\n")