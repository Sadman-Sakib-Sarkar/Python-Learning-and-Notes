from django.db import models #This package stores all the method for using databases
from django.utils import timezone

# Create your models here.
# Here our classes will be stored like genre, movie etc.

class Genre(models.Model): 
    #inside the models module there is a Model class
    #it has all the functionalities for storing model objects in the database or retreiving model object filter them and so on
    #by inheriting genre class from model.Model class we can use all the methods of that class
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
        #this __str__ magic method is for returning as object otherwise it will consider every name as object
        #now if we want to add more columns in admin panel then we need to go to the admin.py file

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    #by on_delete we tells django what should happen when the genre is deleted 
    #here we used cascading it means if we delete a genre all the movies under the genre will be deleted
    date_created = models.DateTimeField(default=timezone.now) #here we are passing reference not method to make it dynamically changed time
    #datetime.now() don't know the timezone
    #better approach is to use datetime with timezone

#in future we can add more classes or modify our existing classes
#next step is to tell django to synchronise our database with the models we have defined in the movies app


# To reflect the changes of models in database: python3 manage.py makemigrations
# But it will show no changes detected because we haven't registered our movies app with django
# open our vidly project -> settings.py -> INSTALLED_APPS = [appname.apps.classname.Config]
# apps class name can be found inside the app folder -> apps.py -> classname.Config

# Next step is to run: python3 manage.py runserver
# It will show that one extra migration is unapplied. That means we have migrations that we need to execute
# So stop the server with cntrl+c
# run: python3 manage.py migrate 
# It will execute all the pending migration on our database


