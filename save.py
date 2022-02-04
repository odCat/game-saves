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


def create_saves_folder():
    saves_folder = 'saves'
    if not os.path.isdir(saves_folder):
        os.mkdir(saves_folder)


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


def game_save_paths_file_exists(path='games.json'):
    if os.path.exists(path):
        return True
    else:
        return False


if __name__ == '__main__':
    pass

# TODO
# Does shutil.copytree need a try/catch block?
