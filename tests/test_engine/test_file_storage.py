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
        assertIsNone(available_models)
        assertNotIsInstance(available_models, BaseModel)

    def test_new(self):
        '''
        Tests the addition of a
        new object in the File
        '''
        compactFile = FileStorage()
        assertIs(compactFile, FileStorage)
        testObject = BaseModel()
        assertIs(testObject, BaseModel)
        prev = compactFile.all()
        compactFile.new(testObject)
        '''
        Make sure a BaseModel is being inserted
        '''
        assertIsNotNone(testObject.id)
        '''
        Make sure it is saved in the file/ __objects
        '''
        newFileStorage = compactFile.all()
        key = "{}.{}".format('BaseModel', testObject.id)
        assertIn(key, newFileStorage.keys())
        assertNotEqual(prev, newFileStorage)

    def test_save(self):
        '''
        unittest the save method
        '''
        file_ = FileStorage()
        assertIs(file_, FileStorage)
        '''
        shouldn't return anything...
        '''
        assertTrue(file_.save())

    def test_reload(self):
        '''
        unittest reload
        '''
        file__ = FileStorage()

        assertIsInstance(file__, FileStorage)
        assertTrue(file__.reload())


if __name__ == '__main__':
    unittest.main()
