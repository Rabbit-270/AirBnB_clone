#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
	'''
  	unittests to make sure that the
 	User class operates accordingly.
  	'''
  	def test_constructor(self):
    	'''
    	Unittests for testing the Constructor
    	of a User object
    	'''
	    FirstUser = User()
	    self.assertIs(FirstUser, BaseModel)
	    self.assertIs(FirstUser, User)

	  def test_to_dict(self):
	    '''
	    Unittests for testing if the to_dict()
	    class method works for User object.
	    '''
	    FirstUser = User()
	    FirstUser.tested = False
	    returnedDict = FirstUser.to_dict()
	    if self.assertTrue(hasattr(FirstUser,"tested")) == True:
	      FirstUser.tested = False

	  def test_save(self):
	    '''
	    Tests if the save() class method
	    if it works.
	    '''
	    FirstUser = User()
	    FirstUser.tested = False
	    prev_updated_at = FirstUser.updated_at
	    FirstUser.save()
	    new_updated_at = FirstUser.updated_at
	    self.assertNotEqual(prev_updated_at, new_updated_at)


if __name__=='__main__':
  unittest.main()
