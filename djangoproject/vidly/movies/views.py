from django.http import HttpResponse #for returning view function response
from django.shortcuts import render

# Create your views here.

#Its a function that represents our main page. Name can be anything but index is commonly used.
#request is a http request object here that will be passed.
#every view function will return http response
def index(request):
    return HttpResponse("Hello World") #After this we need to map it to url (need to create urls.py file)
