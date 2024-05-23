#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User


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
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    objectDict = json.load(file)

                    for key, val in objectDict.items():
                        className, objId = key.split(".")

                        cls = eval(className)
                        isinstance = cls(**val)

                        FileStorage.__objects[key] = isinstance
                except Exception:
                    pass
