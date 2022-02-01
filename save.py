#!python

import os
import json


def load_game_paths(file_name):
    with open(file_name, 'r') as file:
        result = file.read()
    return json.loads(result)


def game_has_folder(game_name):
    path = 'saves' + '/' + game_name
    if os.path.isdir(path):
        return True
    else:
        return False


if __name__ == '__main__':
    pass
