from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location

def home(request):
    images=Image.get_all_images()
    locations=Location.get_locations()

    return render(request, 'all_gallery/home.html',{"images":images,"locations":locations})

def all_locations(request):
    locations=Location.get_locations()
    return render(request,'all_gallery/home.html',{"locations":locations})