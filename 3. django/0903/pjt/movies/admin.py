from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'overview', 'poster_path')


admin.site.register(Movie, MovieAdmin)