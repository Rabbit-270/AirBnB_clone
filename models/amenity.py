#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    Amenity class inheriting from BaseModel class
    '''
    def __init__(self, *args, **kwargs):
        ''' Constructor '''
        super(Amenity, self).__init__(*args, **kwargs)
        self.name = ""
