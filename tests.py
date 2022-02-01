#!python

import os
import unittest
import save


class TestSave(unittest.TestCase):

    def setUp(self):
        self.temporary_file = 'temporary.json'
        with open(self.temporary_file, 'w') as file:
            test_text = '{"test_name": "test/path"}'
            file.write(test_text)

    def tearDown(self):
        if os.path.exists(self.temporary_file):
            os.remove(self.temporary_file)
        else:
            print('File not found')

    def test_should_read_game_save_paths(self):
        expected = {'test_name': 'test/path'}
        self.assertEqual(expected, save.load_game_paths(self.temporary_file))
