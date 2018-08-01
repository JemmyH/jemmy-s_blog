from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('user_info/', views.user_info, name='user_info'),
    path('logout/',views.logout,name='logout'),
]
