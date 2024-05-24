#!/usr/bin/python3
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
    Store data for later use
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, object):
        """
        Create new record
        """
        objClassName = object.__class__.__name__
        key = "{}.{}".format(objClassName, object.id)

        FileStorage.__objects[key] = object

    def all(self):
        """
        Retrieve records in file storage
        """
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file
        """
        allObjects = FileStorage.__objects
        objectDict = {}

        for x in allObjects.keys():
            objectDict[x] = allObjects[x].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objectDict, file)
            file.write("\n")

    def reload(self):
        """ """
        Read_data = None
        with open(FileStorage.__file_path, encoding="utf-8") as file:
            Read_data = json.load(file)
        for key, value in Read_data.items():
            className, id = key.split(".")

            if className == 'User':
                FileStorage.__objects[key] = User(**value)
            elif className == 'State':
                FileStorage.__objects[key] = State(**value)
            elif className == 'City':
                FileStorage.__objects[key] = City(**value)
            elif className == 'Amenity':
                FileStorage.__objects[key] = Amenity(**value)
            elif className == 'Place':
                FileStorage.__objects[key] = Place(**value)

        print(FileStorage.__objects)

