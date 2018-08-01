from django.urls import path
from . import views

urlpatterns = [
	path('', views.netease_index, name='netease'),
	path('search/', views.neteaseresearch, name='search'),
]