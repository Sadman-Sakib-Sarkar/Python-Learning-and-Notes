from django.contrib import admin
from .models import Movie, Genre #need to import the models that we will register

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') #list_display is for displaying the columns in admin panel
    # After creating the GenreAdmin class we need to register the class in admin

class MovieAdmin(admin.ModelAdmin):
    # Here we can use fields attribute to show the fields like: fields = ('title', 'genre')
    # Or we can exclude some fields like. Here we will exclude the date_created field
    exclude = ('date_created', ) # We need to add a comma other wise python will not consider it as tuple. Python will consider it as a string with paranthysis.
    list_display = ('title', 'number_in_stock', 'daily_rate')

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin) 

# After adding the tables when we will add any record there we will see records as object. To fix this we need to override the __str__ method in genre/movies class

# to add more columns in admin panel:
    # to customize how we work with genre in admin panel we need to create another class as GenreAdmin (naming convention)