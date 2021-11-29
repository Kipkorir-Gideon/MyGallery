from django.shortcuts import render, redirect,get_object_or_404
from .models import Image,Location,Category
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def photos(request):
    category=request.GET.get('category')
    if category==None:
        photos=Image.objects.all()
    else:
        photos=Image.objects.filter(category__category_name=category)


    categories = Category.objects.all()
    return render(request, 'home.html', {'photos': photos, 'categories': categories})


def image_detail(request,photo_id):
  locations = Location.objects.all()

  try:
    photo = get_object_or_404(Image, pk =photo_id)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'home.html', {'photo':photo,"locations":locations})


def category(request):
    category=request.GET.get('category')
    if category==None:
        photos=Image.objects.all()
    else:
        photos=Image.objects.filter(category__category_name=category)


    categories = Category.objects.all()
    return render(request, 'category.html', {'photos': photos, 'categories': categories})


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