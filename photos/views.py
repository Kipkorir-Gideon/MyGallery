from django.shortcuts import render, redirect
from .models import Image,Location,Category
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def gallery(request):
    photos = Image.objects.all()
    date = dt.date.today()
    return render(request, 'home.html', {'photos': photos, 'date': date})
