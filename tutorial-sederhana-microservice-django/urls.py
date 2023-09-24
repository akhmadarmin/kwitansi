urls.py project 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

path('admin/', admin.site.urls),
path('film/', include('film.urls')), 
]

urls.py apps 

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
path('', include(router.urls)),
]