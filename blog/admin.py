from django.contrib import admin
from .models import BlogType, Blog

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_type')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_updated_time')