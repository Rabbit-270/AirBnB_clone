#!/usr/bin/python3
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    '''
    unittests for City class.
    '''
    def test_constructor(self):
        ''' tests if an object is a City. '''
        City_1 = City()
        self.assertIs(City_1, City)

    def test_attributes(self):
        ''' unittests for object attributes. '''
        City_2 = City()
        City_2.state_id = 34
        City_2.name = "San Francisco"
        self.assertTrue(hasattr(City_2, "state_id"))
        self.assertTrue(hasattr(City_2, "name"))


if __name__ == "__main__":
    unittest.main()
