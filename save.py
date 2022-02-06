#!python

#   Copyright 2022 Mihai Gătejescu
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


def copy_save_file(source, target):
    shutil.copytree(source, target)


def generate_name():
    result = datetime.datetime.now().date().isoformat()
    result += ' ' + str(datetime.datetime.now().hour)
    result += ':' + str(datetime.datetime.now().minute)
    result += ':' + str(datetime.datetime.now().second)
    return result


def create_saves_folder_if_doesnt_exist():
    create_folder_if_doesnt_exist('saves')


def save():
    create_saves_folder_if_doesnt_exist()
    root = 'saves'
    games_and_paths = load_game_paths()

    for game in games_and_paths:
        create_folder_if_doesnt_exist(root + '/' + game)


def clean():
    shutil.rmtree('saves')


if __name__ == '__main__':
    pass

# TODO
# Does shutil.copytree need a try/catch block?
# Hook clean to git clone
# Is there an option to not trigger the hook when cloning?
