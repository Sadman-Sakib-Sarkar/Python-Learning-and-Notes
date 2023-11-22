#We will create urlpatterns variable of list and its a convention that django expects us to follow
#in this list we will create path objects that will map url end points to our view functions
    #For this we need to use path function of django
from django.urls import path
from . import views #This is a better way in django to imoprt. Dot means the current directory

## Url Configuration:
#Here we can pass one or more path objects. Every app will have a url configuraion.
urlpatterns = [
    path('', views.index, name='index'), #Here views.index is reference not calling the function
    #Empty string will represent the root of the app
    #We need to map this with a view function so that we need to import index function from our views module
    #name='index' is the best practice to give name to url end points
]

#After that we need to go to the main apps urls.py file that defines urls configuration of our main app