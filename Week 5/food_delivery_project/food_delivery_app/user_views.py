from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Restaurant, Dish
from rest_framework.decorators import api_view
from .serializers import RestaurantSerializer, DishSerializer
from rest_framework.response import Response
import json


# Create your views here.
@api_view(['GET'])
def list_all_dishes(request):
    # get details about a particular restaurant
    dish = Dish.objects()
    serializer = DishSerializer(dish, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_restaurant(request):
    # get details about a particular restaurant
    dish = Dish.objects()
    serializer = DishSerializer(dish, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_dish_in_restaurant(request):
    # get details about a particular restaurant
    dish = Dish.objects()
    serializer = DishSerializer(dish, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_dish_across_restaurants(request):
    # get details about a particular restaurant
    dish = Dish.objects()
    serializer = DishSerializer(dish, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def place_order(request):
    # get details about a particular restaurant
    dish = Dish.objects()
    serializer = DishSerializer(dish, many=True)
    return Response(serializer.data)



