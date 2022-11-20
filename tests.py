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
import unittest

import save


class TestSave(unittest.TestCase):

    temporary_file = 'temporary.json'

    @classmethod
    def setUpClass(cls):
        save.create_saves_folder_if_doesnt_exist()
        with open(cls.temporary_file, 'w') as file:
            test_text = '{"test_name": "test/path"}'
            file.write(test_text)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.temporary_file):
            os.remove(cls.temporary_file)
        else:
            print('File not found')

    def test_should_read_game_save_paths(self):
        expected = {'test_name': 'test/path'}
        self.assertEqual(expected, save.load_game_paths(self.temporary_file))

    def test_should_return_true_if_folder_exists(self):
        self.assertTrue(save.folder_exists('saves'))

    def test_should_return_false_if_folder_exists(self):
        self.assertFalse(save.folder_exists('does_not_exist'))

    def test_should_return_true_if_file_exists(self):
        self.assertTrue(save.file_exists(self.temporary_file))

    def test_should_return_false_if_file_exists(self):
        self.assertFalse(save.file_exists('does_not_exist'))


if __name__ == '__main__':
    unittest.main()
