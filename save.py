#!python

import os
import json
import shutil

import datetime


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


def create_game_folder(game_name):
    path = 'saves/' + game_name
    os.mkdir(path)


def copy_save_file(source, target):
    shutil.copytree(source, target)


def generate_folder_name():
    result = datetime.datetime.now().date().isoformat()
    result += ' ' + str(datetime.datetime.now().hour)
    result += ':' + str(datetime.datetime.now().minute)
    result += ':' + str(datetime.datetime.now().second)
    return result


if __name__ == '__main__':
    pass

# TODO
# Does shutil.copytree need a try/catch block?
# Is it needed to use the name to generate the name of the saves folder?
