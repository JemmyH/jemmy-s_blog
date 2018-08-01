from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from mdeditor.fields import MDTextField
from record_message.models import ReadNumExpandMethod, ReadDetail


# Create your models here.
class BlogType(models.Model):
    blog_type = models.CharField(max_length=30)

    def __str__(self):
        return self.blog_type


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    read_num = models.IntegerField(default=0)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    content = MDTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_time']
