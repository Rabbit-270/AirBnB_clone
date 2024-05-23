#!/usr/bin/python3
from models.base_model import BaseModel
from models.amenity import Amenity
from unittest


class TestAmenity(unittest.TestCase):
    ''' unittests for Amenity child class '''
    def test_constructor(self):
        ''' asserts the constructor(s) and other attributes. '''
        Amenity1 = Amenity()
        self.assertIs(Amenity1, Amenity)

    def test_attributes(self):
        ''' asserts attributes and their existance. '''
        Amenity2 = Amenity()
        self.assertEqual(Amenity2.name, "")
        Amenity2.name = "Swimming Pool"
        self.assertTrue(hasattr(Amenity2, "name"))
        self.assertNotNone(Amenity2.name)


if __name__ == "__main__":
    unittest.main()
