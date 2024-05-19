#!/usr/bin/python3
"""
Base model
"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initialize the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        instanceDict = self.__dict__.copy()
        instanceDict["__class__"] = self.__class__.__name__
        instanceDict["created_at"] = self.created_at.isoformat()
        instanceDict["updated_at"] = self.updated_at.isoformat()

        return instanceDict

    def __str__(self):
        """
        Print in string format
        """
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)


if __name__ == "__main__":
    myModel = BaseModel()
    myModel.name = "My_First_Model"
    myModel.my_number = 89
    print(myModel)
    myModel.save()
    print(myModel)
    modelJson = myModel.to_dict()
    print(modelJson)
    print("JSON of myModel:")
    for i in modelJson.keys():
        print("\t{}: ({}) - {}".format(i, type(modelJson[i]), modelJson[i]))
