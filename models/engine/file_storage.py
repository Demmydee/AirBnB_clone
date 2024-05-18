#!/usr/bin/python3
""" base_model """
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key(i) <obj class name>.id"""
        i = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[i] = obj
        # return FileStorage.__objects

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        tempDict = {}
        # >>> _objects = {'ob.11': obj1, 'ob.22': obj2,...}
        for obj in FileStorage.__objects:
            tempDict[obj] = FileStorage.__objects[obj].to_dict()
            # >>> tempDict = {'ob.11': {'id': 11, 'name': aa,...},
            # {'id': 11, 'name': aa,...},...}
        with open(FileStorage.__file_path, "w") as dbFP:
            json_text = json.dumps(tempDict)
            dbFB.write(json_text)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""

        try:
            with open(FileStorage.__file_path) as dbFB:
                tempDict = json.load(dbFB)
                for val in tempDict.values():
                    # convert val to object of class __class__
                    # since new(self, obj) method
                    # accepts obj as parameter
                    cls_name = val["__class__"]
                    # delete __class__ key since we dont need it
                    # it will be generated every time we use to_dict()
                    del val["__class__"]
                    self.new(eval(cls_name)(**val))
        except Exception as e:
            # except FileNotFoundError:
            return
