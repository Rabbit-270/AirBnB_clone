#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    '''
    City inherits from BaseModel.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor of this City class.
        '''
        if kwargs == {}:
            super(City, self).__init__(*args, **kwargs)
            self.state_id = ""
            self.name = ""
        else:
            for key, value in kwargs.items():
                self.key = value
            super(City, self).__init__(**kwargs)
