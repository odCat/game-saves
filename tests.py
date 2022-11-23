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
import shutil
import unittest

import save


def remove_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    else:
        print('Folder not found')


def remove_file(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        print('File not found')


class TestSave(unittest.TestCase):

    games_paths_test_file = 'temporary.json'
    test_game = 'test_game'
    test_save = 'test_save'
    test_path = './test'
    test_root = 'saves'

    @classmethod
    def setUpClass(self):
        save.create_saves_folder_if_doesnt_exist()
        with open(self.games_paths_test_file, 'w') as file:
            test_text = '{"game1": "path1", "game2": "path2"}'
            file.write(test_text)
        save.create_folder_if_doesnt_exist(self.test_path)
        with open(self.test_path + '/' + self.test_save, 'w') as file:
            test_text = 'This ia a test save file'
            file.write(test_text)

    @classmethod
    def tearDownClass(self):
        remove_file(self.games_paths_test_file)
        remove_folder(self.test_path)
        remove_folder(self.test_root + '/' + self.test_game)

    def test_should_read_game_save_paths(self):
        expected = {'game1': 'path1', 'game2': 'path2'}
        self.assertEqual(expected, save.load_game_paths(self.games_paths_test_file))

    def test_should_return_true_if_folder_exists(self):
        self.assertTrue(save.folder_exists('saves'))

    def test_should_return_false_if_folder_exists(self):
        self.assertFalse(save.folder_exists('does_not_exist'))

    def test_should_return_true_if_file_exists(self):
        self.assertTrue(save.file_exists(self.games_paths_test_file))

    def test_should_return_false_if_file_exists(self):
        self.assertFalse(save.file_exists('does_not_exist'))

    def test_search_game(self):
        games_and_paths = {'game1': 'path1', 'game2': 'path2'}
        self.assertTrue(save.search_game('game1', games_and_paths))
        self.assertFalse(save.search_game('game3', games_and_paths))

    def test_save_one_game(self):
        save.save_one_game(self.test_game, self.test_path, self.test_root)
        save_folder = self.test_root + '/' + self.test_game
        self.assertTrue(save.folder_exists(save_folder))
        self.assertTrue(save.file_exists(save_folder + '/' + self.test_save))


if __name__ == '__main__':
    unittest.main()
