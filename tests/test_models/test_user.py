#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    '''
    unittests to make sure that the
    User class operates accordingly.
    '''
    def test_contructor(self):
        '''
        Unittests to make sure that the
        User class object is created.
        '''
        FirstUser = User()
        self.assertIs(FirstUser, BaseModel)
        self.assertIs(FirstUser, User)

    def test_to_dict(self):
        '''
        Unittests for testing if the to_dict()
        class method works for User object.
        '''
        SecondUser = User()
        SecondUser.tested = False
        returnedDict = SecondUser.to_dict()
        if self.assertTrue(hasattr(returnedDict, "tested")) is True:
            SecondUser.tested = True

    def test_save(self):
        '''
        Tests if the save() class method works.
        '''
        ThirdUser = User()
        prev_updated_at = ThirdUser.updated_at
        ThirdUser.save()
        new_updated_at = ThirdUser.updated_at
        self.assertIsNotEqual(prev_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
