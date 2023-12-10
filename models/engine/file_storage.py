#!/usr/bin/python3
"""our storage engine"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def class_list(self):
        """Returns a dictionary of valid list of the classes
        and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return class_list

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing)
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)

            for key, value in loaded_objects.items():
                class_name, obj_id = key.split('.')
                obj_class = eval(class_name)  # Convert string to class
                # Create instance using the dictionary
                obj_instance = obj_class(**value)
                self.__objects[key] = obj_instance
        """
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: self.class_list()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            self.__objects = obj_dict

        except FileNotFoundError:
            pass  # If the file doesn't exist, do nothing
