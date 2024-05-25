#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    '''
    State class inherits from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor of the State class.
        '''
        if kwargs == {}:
            super(State, self).__init__(*args, **kwargs)
            self.name = ""
        else:
            for key, value in kwargs.items():
                self.key = value
            super(State, self).__init__(*args, **kwargs)
