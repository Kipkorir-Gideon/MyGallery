from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.photos,name='homePage'),
    path('search/', views.search_results, name='search_results'),
    path('search/location/',views.search_by_location, name='search_by_location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)