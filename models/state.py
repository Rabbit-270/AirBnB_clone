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
        super(State, self).__init__(*args, **kwargs)
        self.name = ""
