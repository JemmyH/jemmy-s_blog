from django.urls import path
from . import views

urlpatterns = [
    path('', views.echo_index, name='echo'),
    path('parse_song/', views.parse_song, name='parse_song'),
    path('echo_name_index', views.echo_name_index, name='echo_name_index'),
    path('search_song/', views.search_song, name='search_song')
]
