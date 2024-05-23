#!/usr/bin/python3
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    ''' unittests for the Review class. '''
    def test_constructor(self):
        ''' asserts a new object. '''
        FirstReview = Review()
        self.assertIs(FirstReview, Review)
        self.assertIsNotNone(FirstReview)

    def test_attributes(self):
        SecondReview = Review()
        self.assertEqual(SecondReview.place_id, "")
        self.assertEqual(SecondReview.user_id, "")
        self.assertEqual(SecondReview.text, "")


if __name__ == "__main__":
    unittest.main()
