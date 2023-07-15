#!/usr/bin/python3
"""FileStorage class."""
import json
from models import base_model, user
from os.path import exists

BaseModel = base_model.BaseModel
User = user.User
name_class = ["BaseModel","User"]


class FileStorage:
    """FileStorage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return FileStorage objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Set objects with keys and values
        """
        class_name = obj.__class__.__name__
        id = obj.id
        class_id = class_name + "." + id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """
        write data to json file
        """
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            json.dump(dict_to_json, f)

    def reload(self):
        """
        Deserialize json to python objects if filepath exist
        """
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                dic_obj = json.load(f)
                for key, value in dic_obj.items():
                    class_name = key.split(".")[0]
                    if class_name in name_class:
                        FileStorage.__objects[key] = eval(class_name)(**value)
                    else:
                        pass
