#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary or a list of objects of one type of class.

        Args:
            cls (type): The class type to filter objects.

        Returns:
            dict or list: If cls is None, returns the entire dictionary
                          of objects. Otherwise, returns a list of objects
                          of the specified class.
        """
        if cls is None:
            return FileStorage.__objects

        filtered_objects = {key: obj for key, obj in FileStorage.__objects.items()
                            if isinstance(obj, cls)}
        return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.all()[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(serialized_objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, val in serialized_objects.items():
                    cls_name = val['__class__']
                    if cls_name in classes:
                        self.all()[key] = classes[cls_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists"""
        if obj is not None:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)
