from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'food_delivery_app/index.html')


def about(request):
    return HttpResponse("We are at about")


def contact(request):
    return HttpResponse("We are at contact")


def tracker(request):
    return HttpResponse("We are at tracker")


def search(request):
    return HttpResponse("We are at search")


def food_view(request):
    return HttpResponse("We are at food view")


def checkout(request):
    return HttpResponse("We are at checkout")
