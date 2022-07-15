from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Restaurant, Dish
from rest_framework.decorators import api_view
from .serializers import RestaurantSerializer, DishSerializer
from rest_framework.response import Response
import json


# Create your views here.
@api_view(['GET'])
def restaurant_info(request, restaurant_id: int):
    # get details about a particular restaurant
    restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
    serializer = RestaurantSerializer(restaurant, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def list_restaurant_dishes(request, restaurant_id: int):
    # get all the dishes in a particular restaurant
    dish = Dish.objects(restaurant_id=restaurant_id)
    serializer = DishSerializer(dish, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_dish(request, restaurant_id: int):
    converted_request = json.loads(request.body)
    dish = Dish()
    dish.dish_id = converted_request['dish_id']
    dish.restaurant_id = converted_request['restaurant_id']
    dish.name = converted_request['name']
    dish.description = converted_request['description']
    dish.dish_image = converted_request['dish_image']
    dish.category = converted_request['category']
    dish.cuisine = converted_request['cuisine']
    dish.availability = converted_request['availability']
    dish.availability_time = converted_request['availability_time']
    dish.save()
    serializer = DishSerializer(dish, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def modify_dish(request, restaurant_id: int, dish_id: int):
    dish = Dish.objects(dish_id=dish_id)
    serializer = DishSerializer(instance=dish, data=request.body)
    if serializer.is_valid():
        for obj in serializer:
            obj.save()
    return Response(serializer.data)
