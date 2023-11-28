from django.http import HttpResponse #for returning view function response
from django.shortcuts import render # This render method is used for render template
from .models import Movie 
# Database Abstraction API
# The model class gives us an api(aplication programming interface) and this api abstracts away the complexity to working with database
# Using this api we can get the list of objects from database and can perform CRUD operations.



# Create your views here.

#Its a function that represents our main page. Name can be anything but index is commonly used.
#request is a http request object here that will be passed.
#every view function will return http response
def index(request):
    # Movie.objects.all() # This will get all the movie objects of our database
    # # django generates SQL command like: SELECT * FROM movies_movie

    # Movie.objects.filter(release_year=1984)
    # # SELECT * FROM movies_movie WHERE release_year=1984

    # #For getting single object:
    # Movie.objects.get(id=1)

    # movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies]) 
    # return HttpResponse(output)

    # return HttpResponse("Hello World") #After this we need to map it to url (need to create urls.py file)

    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies}) #render takes 3 parameter (request, template, context which is dictionary to send data to the template page)
    # We have created a templates folder inside the movies app. By default django looks at the templates folder
    
