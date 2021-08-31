from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('introduce/', views.introduce, name='introduce'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('image/', views.image),
    path('templates_language/', views.templates_language),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
