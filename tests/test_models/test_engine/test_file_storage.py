import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)

    def tearDown(self):
        self.storage._FileStorage__objects = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIn(self.obj1, all_objects.values())
        self.assertIn(self.obj2, all_objects.values())

    def test_new(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        all_objects = self.storage.all()
        self.assertIn(new_obj, all_objects.values())

    def test_save_reload(self):
        self.storage.save()
        with open(self.file_path, "r") as f:
            data = json.load(f)
            self.assertIn(f"{BaseModel.__name__}.{self.obj1.id}", data)
            self.assertIn(f"{BaseModel.__name__}.{self.obj2.id}", data)

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn(self.obj1.id, [obj.id for obj in all_objects.values()])
        self.assertIn(self.obj2.id, [obj.id for obj in all_objects.values()])


if __name__ == "__main__":
    unittest.main()

