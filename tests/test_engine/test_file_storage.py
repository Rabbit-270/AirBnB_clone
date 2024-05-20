#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileEngine(unittest.TestCase):
    '''
Test cases for file_storage
    '''
    def test_all(self):
        localStorage = FileStorage()
        available_models = localStorage.save()
        '''
        the file should not be empty; False
        '''
        assertIsNone(available_models)


if __name__ == '__main__':
    unittest.main()
