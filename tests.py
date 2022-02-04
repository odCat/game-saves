#!python

import os
import unittest

import save


class TestSave(unittest.TestCase):

    temporary_file = 'temporary.json'

    @classmethod
    def setUpClass(cls):
        save.create_saves_folder()
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
        self.assertTrue(save.game_has_folder(''))

    def test_should_return_false_if_folder_exists(self):
        self.assertFalse(save.game_has_folder('does_not_exist'))

    def test_should_return_false_if_file_exists(self):
        self.assertFalse(save.game_save_paths_file_exists('does_not_exist'))

    def test_should_return_true_if_file_exists(self):
        self.assertTrue(save.game_save_paths_file_exists(self.temporary_file))


if __name__ == '__main__':
    unittest.main()
