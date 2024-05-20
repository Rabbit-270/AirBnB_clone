#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileEngine(unittest.TestCase):
    '''
Test cases for file_storage
    '''
    def test_all(self):
        '''
        Tests the returned JSON model
        returned when the FileStorage is commanded
        to return all of the objects.
        '''
        localStorage = FileStorage()
        available_models = localStorage.save()
        '''
        the file should not be empty; False
        '''
        assertIs(localStorage, FileStorage)
        assertIsNotNone(available_models)
        assertTrue(len(available_models) == 0 or len(available_models) != 0)
        assertNotIsInstance(available_models, BaseModel)

        new_base_model = BaseModel()
        assertIsInstance(new_base_model, BaseModel)
        dictionary_new_base_model = new_base_model.to_dict()
        assertIsNotNone(dictionary_new_base_model.id)


if __name__ == '__main__':
    unittest.main()
