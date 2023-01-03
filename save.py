#!python

#   Copyright 2022, 2023 Mihai Gătejescu
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License

import os
import json
import shutil
import datetime
from sys import exit as sys_exit


def folder_exists(folder_path):
    if os.path.isdir(folder_path):
        return True
    else:
        return False


def create_folder(folder_path):
    if not folder_exists(folder_path):
        os.mkdir(folder_path)


def create_folder_if_doesnt_exist(folder_name):
    create_folder(folder_name)


def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False


def load_game_paths(file_path='games.json'):
    if not file_exists(file_path):
        print('Game saves path file was not found.')
        sys_exit()
    else:
        with open(file_path, 'r') as file:
            result = file.read()
        return json.loads(result)


def copy_save_files(source, target):
    shutil.copytree(source, target)


def generate_name():
    result = datetime.datetime.now().date().isoformat()
    result += ' ' + str(datetime.datetime.now().hour)
    result += str(datetime.datetime.now().minute)
    result += str(datetime.datetime.now().second)
    return result


def create_saves_folder_if_doesnt_exist():
    create_folder_if_doesnt_exist('saves')


def setup_root_folder(root='saves'):
    create_saves_folder_if_doesnt_exist()
    return root


def search_game(game, games_and_paths):
    return game in games_and_paths


def search_game_in_dict(game):
    games_and_paths = load_game_paths()
    return search_game(game, games_and_paths)


def save():
    root = setup_root_folder()
    games_and_paths = load_game_paths()

    for game, path in games_and_paths.items():
        if not folder_exists(path):
            print('The saves for {} could not be found.'.format(game))
            continue
        game_folder = root + '/' + game
        create_folder_if_doesnt_exist(game_folder)
        copy_save_files(path, game_folder + '/' + generate_name())
        print('{} {} backed up'.format(game, '...' + (27 - len(game))*'.'))


def save_one_game(game, path, root):
    root = setup_root_folder(root)

    if not folder_exists(path):
        print('The saves for {} could not be found.'.format(game))
    else:
        game_folder = root + '/' + game
        copy_save_files(path, game_folder)


def call_save_one_game(game):
    root = setup_root_folder()
    games_and_paths = load_game_paths()
    game_folder = root + '/' + game
    create_folder_if_doesnt_exist(game_folder)

    save_folder = game_folder + '/' + generate_name()
    path = games_and_paths[game]
    save_one_game(game, path, save_folder)
    print('{} {} backed up'.format(game, '...' + (27 - len(game)) * '.'))


def clean():
    shutil.rmtree('saves')


if __name__ == '__main__':
    save()

# TODO
# Does shutil.copytree need a try/catch block? Yes
# Use arguments
# Improve handling of missing saves
# Compare saves
# Remove the older saves
# Make it work for Windows
# Switch to use a class
# Add GUI
