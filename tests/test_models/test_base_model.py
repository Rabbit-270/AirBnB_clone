#!/usr/bin/python3
"""
Test base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        myModel = BaseModel()

        self.assertIsNotNone(myModel.id)
        self.assertIsNotNone(myModel.created_at)
        self.assertIsNotNone(myModel.updated_at)

    def test_save(self):
        myModel = BaseModel()

        initialUpdatedAt = myModel.updated_at
        currentUpdatedAt = myModel.save()

        self.assertNotEqual(initialUpdatedAt, currentUpdatedAt)

    def test_to_dict(self):
        model = BaseModel()

        modelDic = model.to_dict()

        self.assertIsInstance(modelDic, dict)
        self.assertEqual(modelDic["__class__"], "BaseModel")
        self.assertEqual(modelDic["id"], model.id)
        self.assertEqual(modelDic["created_at"], model.created_at.isoformat())
        self.assertEqual(modelDic["updated_at"], model.updated_at.isoformat())

    def test_str(self):
        myModel = BaseModel()

        self.assertTrue(str(myModel).startswith("[BaseModel]"))
        self.assertIn(myModel.id, str(myModel))
        self.assertIn(str(myModel.__dict__), str(myModel))


if __name__ == "__main":
    unittest.main()
