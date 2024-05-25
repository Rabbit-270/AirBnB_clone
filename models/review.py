#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Review child class inheritting from BaseModel class. '''
    def __init__(self, *args, **kwargs):
        ''' constructor '''
        if kwargs == {}:
            super(Review, self).__init__(*args, **kwargs)
            self.place_id = ""
            self.user_id = ""
            self.text = ""
        else:
            for key, value in kwargs.items():
                self.key = value
            super(Review, self).__init__(*args, **kwargs)
