from django.urls import path
from . import views

urlpatterns = [
    path('', views.luoo_index, name='luoo'),
    path('check_luoo/', views.search_luowang, name='check_luoo'),
    path('test/',views.test,name='test')
]
