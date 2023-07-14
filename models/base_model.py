#!/usr/bin/python3
"""
    BaseModel that defines all common attriutes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
      Represents the BaseModel
      Attributes:
        id (str): str uuid.uuidv4 uunique identifier
        created_at (date): displays the time when the instance was created
        updated_at (date): displays the time when the instance was created
        and everytime it is changed
    """
    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel
        Args:
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()  # generated once
        self.updated_at = datetime.now()  # generated with every change

    def __str__(self):
        """ Define the representation of a BaseModel """
        return ('[{}] ({}) {}'.format(
            type(self).__name__,
            self.id,
            self.__dict__)
        )

    def save(self):
        """ Updates the public instance attribute updated_at with the
            current datetime
        """
        self.updated_at = datetime.now()  # generated with every change
        return self.updated_at

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
            of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
