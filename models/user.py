#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Inherits from BaseModel
    '''
    def __init__(self, **kwargs):
        ''' constructor '''
        super(User, self).__init__(**kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
