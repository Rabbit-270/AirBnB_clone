#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Created objects --")
print("-- User --")
my_user = User()
my_user.first_name = "Nick"
my_user.last_name = "Jamon"
my_user.email = "airtime@gmail.com"
my_user.password = "rootz"
my_user.save()
print(my_user)

print("-- State --")
my_state = State()
my_state.name = "California"
my_state.save()
print(my_state)

print("-- City --")
my_city = City()
my_city.state_id = "Cal"
my_city.name = "San Francisco"
my_city.save()
print(my_city)

print("-- Amenity --")
my_amenity = Amenity()
my_amenity.name = "Swimming pool"
my_amenity.save()
print(my_amenity)

print("-- Place --")
my_place = Place()
my_place.city_id = "S.F"
my_place.user_id = "N"
my_place.name = "Joe's Inn"
my_place.description = "Georgeous villa on the hills on Sunny San Francisco."
my_place.number_rooms = 2
my_place.number_bathrooms = 3
print(my_place)

print("-- Review --")
my_review = Review()
my_review.place_id = "JI"
my_review.user_id = "N"
my_review.text = "Could do with a bit of life. "
print(my_review)
