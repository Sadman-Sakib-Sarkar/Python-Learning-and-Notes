from django.http import HttpResponse, Http404 
#HttpResponse for returning view function response
#Http404 for raise 404 page not found exception
from django.shortcuts import render, get_object_or_404
#render method is used for render template
#get_object_or_404 is used for shortcut of raising 404 exception
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
    
#when we request like movies/1 django will pass movie_id=1 to this view function
def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id) # we can use id or pk both (pk = primary key)
    #     #it will give a movie object of that id. then we will put it into a template, render it and return the result
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()

    ## We have shortcut for raise 404 page not found. import get_objectt_or_404 from django.shortcuts
    movie = get_object_or_404(Movie, pk=movie_id) #here the first argument is the model class. here Movie
    return render(request, 'movies/detail.html', {'movie': movie})

