from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('index/', views.index),
    path('', views.index),  # https://127.0.0.1:8000/articles/ 주소를 의미 (기본 주소)
]
