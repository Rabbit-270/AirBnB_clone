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
        super(City, self).__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
