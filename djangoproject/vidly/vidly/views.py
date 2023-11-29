from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 
    #Here we don't need to add the context because we will not show any data in the home page