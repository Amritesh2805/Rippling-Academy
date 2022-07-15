from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def food_delivery_app_home(request):
    return render(request, 'food_delivery_app/index.html')