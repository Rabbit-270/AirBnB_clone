#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Inherits from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        ''' constructor '''
        if kwargs == {}:
            ''' No arguments. '''
            super(User, self).__init__(*args, **kwargs)
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
        elif kwargs != {}:
            KWARGS = kwargs
            for key, value in KWARGS.items():
                self.key = value
            super(User, self).__init__(*args, **KWARGS)
