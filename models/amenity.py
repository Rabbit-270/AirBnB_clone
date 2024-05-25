#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    Amenity class inheriting from BaseModel class
    '''
    def __init__(self, *args, **kwargs):
        ''' Constructor '''
        if kwargs == {}:
            super(Amenity, self).__init__(*args, **kwargs)
            self.name = ""
        else:
            for key, value in kwargs.item():
                self.key = value
            super(Amenity, self).__init__(*args, **kwargs)
