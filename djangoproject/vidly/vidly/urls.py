"""
URL configuration for vidly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource
from . import views # for the home page

movie_resource = MovieResource()

urlpatterns = [
    path('', views.home),
    path("admin/", admin.site.urls), #Its a separate indipendent app for every project
    #Here we need to pass a new path object
    path("movies/", include('movies.urls')), 
    #we need to import another function from django.urls which is include
    #inside include() function we need to pass the path of url configuration of movies/
    #python will send the 'movies/' to the url location and it will sit inside the "" empty string
    path("api/", include(movie_resource.urls))
]
