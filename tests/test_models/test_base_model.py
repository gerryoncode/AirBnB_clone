import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        obj = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_output)

    def test_save(self):
        obj = BaseModel()
        with patch.object(
                BaseModel,
                'updated_at', datetime(2022, 1, 1)) as mock_updated_at:
            obj.save()
            self.assertEqual(obj.updated_at, mock_updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(datetime.fromisoformat(
            obj_dict['created_at']),
            obj.created_at
        )
        self.assertEqual(datetime.fromisoformat(
            obj_dict['updated_at']),
            obj.updated_at
        )


if __name__ == '__main__':
    unittest.main()
