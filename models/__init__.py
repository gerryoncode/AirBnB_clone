#!/usr/bin/python3
"""
FileStorage instance
"""


from .engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
