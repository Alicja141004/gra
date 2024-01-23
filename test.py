import math
import random
import tempfile
import os
from fun_trees import isCollision, check_and_reset_trees, generate_trees
from fun_leaderboard import sort_dict, read_scores_from_file
def test_sort_dict():
    input_dict = {'A1': 90, 'A2': 80, 'A3': 95, 'A4': 75}
    expected_result = {'A3': 95, 'A1': 90, 'A2': 80, 'A4': 75}

    result = sort_dict(input_dict)

    assert result == expected_result

def test_collision():
    result = isCollision(0, 0, 10, 10, 20, 20, 30, 30)
    assert result is True


def test_reset_trees():
    window_width = 800
    window_height = 600
    tree_width = 50
    tree_height = 50
    trees = [{'x': 100, 'y': -60}]
    check_and_reset_trees(trees, window_width, window_height, tree_width, tree_height)

    assert trees[0]['y'] == window_height



def test_read_scores_from_file():
    content = "Player1, 30.5\nPlayer2, 25.3\nPlayer3, 40.2"
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(content)
        temp_file_path = temp_file.name

    scores = read_scores_from_file(temp_file_path)

    assert scores == {'Player1': 30.5, 'Player2': 25.3, 'Player3': 40.2}

    os.remove(temp_file_path)

def test_generate_trees():
    window_width = 800
    window_height = 600
    tree_width = 50
    tree_height = 50

    trees = generate_trees(window_width, window_height, tree_width, tree_height)

    assert len(trees) == 12

    for tree in trees:
        assert tree['x'] >= 0 and tree['x'] <= window_width - tree_width
        assert tree['y'] >= window_height and tree['y'] <= window_height * 2

