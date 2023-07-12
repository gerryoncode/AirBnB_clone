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

if __name__ == '__main__':
    unittest.main()
