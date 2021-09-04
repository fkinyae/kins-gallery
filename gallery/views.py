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

def image_by_location(request,location):
    images=Image.get_image_by_location(location)
    return render(request,'all_gallery/image_location.html',{"images":images,"location":location})