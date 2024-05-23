#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    '''
    Test Cases for the State class.
    '''
    def test_constructor(self):
        ''' unittests a created state/location '''
        State_1 = State()
        self.assertIs(State_1, State)

    def test_attributes(self):
        ''' checks for certain attributes. '''
        State_2 = State()
        State_2.name = "California"
        self.assertTrue(hasattr(State_2, "name"))


if __name__ == "__main__":
    unittest.main()
