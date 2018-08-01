from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog'),  # 所有最近博客
    path('<int:blog_id>', views.blog_datail, name='blog_detail'),  # 博客详情
    path('type/<int:blog_type_id>', views.blog_type_list, name='blogs_with_type'),
]
