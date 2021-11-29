from django.shortcuts import render, redirect
from .models import Image,Location,Category
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def photos(request):
    photos = Image.objects.all()
    date = dt.date.today()
    return render(request, 'home.html', {'photos': photos, 'date': date})


def category(request, name):
    category = Category.objects.get(name=name)
    photos = Image.objects.filter(category=category).order_by('-time_posted')
    return render(request, 'category.html', {'photos': photos, 'category': category})


def search_by_location(request):
    if 'location' in request.GET and request.GET["location"]:
        image_location = request.GET.get("location")
        searched_images = Image.filter_by_location(image_location)
        message = f"{image_location}"
        print("Image.......",searched_images)
        return render(request, 'location.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image location"
        return render(request, 'location.html', {"message": message})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        category = request.GET.get['category']
        searched_images = Image.search_image(category)
        message = f"{category}"
        return render(request, 'search.html', {"message": message, "searched_images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})