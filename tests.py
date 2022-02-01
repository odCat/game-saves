#!python

import os
import unittest
import save


class TestSave(unittest.TestCase):

    temporary_file = 'temporary.json'

    @classmethod
    def setUpClass(cls):
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
