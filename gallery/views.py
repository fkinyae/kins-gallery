from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def home(request):
    images=Image.get_all_images()
    return render(request, 'all_gallery/home.html',{"images":images})