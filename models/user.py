#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
  '''
  Inherits from BaseModel
  '''
  def __init__(self):
    ''' constructor '''
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
