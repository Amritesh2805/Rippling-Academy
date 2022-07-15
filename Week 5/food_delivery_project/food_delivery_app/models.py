from mongoengine import *


# Create your models here.

class Restaurant(Document):
    restaurant_id = IntField(required=True)
    name = StringField(max_length=100, required=True)
    address = StringField(max_length=100, required=True)
    logo = StringField(max_length=100, required=True)
    cuisine = ListField(StringField(max_length=50))


class Dish(Document):
    dish_id = IntField(required=True)
    restaurant_id = IntField(required=True)
    name = StringField(required=True)
    description = StringField(max_length=100, required=True)
    dish_image = StringField(max_length=100, required=True)
    category = StringField(max_length=100, required=True)
    cuisine = StringField(max_length=100, required=True)
    availability = BooleanField(default=True)
    # restaurant_from = ReferenceField(Restaurant)
    availability_time = ListField(StringField(max_length=50))


dish = Dish(
    dish_id=1,
    restaurant_id=1,
    name='Chicken Wings',
    description='Dummy desc',
    dish_image='dummy image',
    category='Non veg',
    cuisine='Western',
    availability=True
).save()

restaurant = Restaurant(
    restaurant_id=1,
    name='KFC',
    address='dummy address',
    logo='dummy logo',
    cuisine=['Western', 'Non-veg']
).save()
