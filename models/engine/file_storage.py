#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                    {k: v.to_dict()
                        for k, v in FileStorage.__objects.items()}, f
            )

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = key.split(".")[0]
                    cls = eval(cls_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
