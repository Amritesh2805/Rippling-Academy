from mongoengine import *


 # Create your models here.

class Dish(Document):
    name = StringField(max_length=50, required=True)
    dish_id = IntField(required=True)
    category = StringField(max_length=50, required=True)
    image = StringField(max_length=50, required=True)


class Restaurant(Document):
    restaurant_id = IntField(required=True)
    name = StringField(max_length=100, required=True)
    address = StringField(max_length=100, required=True)
    logo = StringField(max_length=100, required=True)
    cuisine = ListField(StringField(max_length=50))

dish = Dish(
    name='Dosa',
    dish_id=1,
    category='South-Indian',
    image='dummy image'
).save()