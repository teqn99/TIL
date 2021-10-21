from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/', views.profile, name='profile'),  # profile은 맨 밑에 설정해야 한다!!(중요) -> login이나 logout같은 아이디로 url 진입시 발생할 수 있는 에러를 방지하기 위해
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
