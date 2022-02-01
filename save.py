#!python

import json


def load_game_paths(file_name):
    with open(file_name, 'r') as file:
        result = file.read()
    return json.loads(result)


if __name__ == '__main__':
    pass
