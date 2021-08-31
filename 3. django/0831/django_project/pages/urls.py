from django.urls import path
from . import views


app_name = 'pages'

urlpatterns = [
    # views.index를 수행하면서 index라는 html을 찾기만 하면 바로 리턴해버림 -> settings에서 적힌 순서대로 읽어오기 때문에 articles의 index가 출력됨
    path('index/', views.index),
    # path('', views.index),
    path('drink/', views.drink),
]