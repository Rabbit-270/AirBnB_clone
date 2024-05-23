#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import City
import unittest


class TestPlace(unittest.TestCase):
    ''' unittests for TestPlace unittest subclass '''
    def test_constructor(self):
        ''' tests object creation '''
        Nora = Place()
        self.assertIs(Nora, Place)

    def test_attributes(self):
        ''' tests attributes. The Place class
        has multiple attributes. '''
        Joe = Place()
        self.assertEqual(Joe.city_id, "")
        self.assertEqual(Joe.user_id, "")
        self.assertEqual(Joe.name, "")
        self.assertEqual(Joe.description, "")
        self.assertEqual(Joe.number_rooms, 0)
        self.assertEqual(Joe.number_bathrooms, 0)
        self.assertEqual(Joe.max_guest, 0)
        self.assertEqual(Joe.price_by_night, 0)
        self.assertEqual(Joe.latitude, 0.0)
        self.assertEqual(Joe.longitude, 0.0)
        self.assertEqual(Joe.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
