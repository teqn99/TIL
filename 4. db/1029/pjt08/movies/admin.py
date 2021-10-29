from django.contrib import admin
from .models import Actor, Review, Movie

# Register your models here.
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Movie)