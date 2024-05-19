#!/usr/bin/python3
"""
Base model
"""


from datetime import datetime
import models
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize the class"""
        timeFormat = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, timeFormat))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

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
    print(myModel.id)
    print(myModel)
    print(type(myModel.created_at))
    print("--")
    modelJson = myModel.to_dict()
    print("JSON of myModel:")
    for i in modelJson.keys():
        print("\t{}: ({}) - {}".format(i, type(modelJson[i]), modelJson[i]))

    print("--")
    my_new_model = BaseModel(**modelJson)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(myModel is my_new_model)
