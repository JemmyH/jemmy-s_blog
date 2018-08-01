from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # 对哪条博客评论
    # 这两条是ContentType创建外键对象使用的，可以方便我们找到Blog，固定格式
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)  # 哪个用户评论的
    comment_time = models.DateTimeField(auto_now_add=True)  # 评论时间
    text = models.CharField(max_length=10000)  # 评论内容

    # # 根评论，如果为空，表示自己本身就是根评论
    # root_comment = models.ForeignKey('self', related_name='root', on_delete=models.CASCADE,default='')
    # # 回复的哪条评论
    # parent_comment = models.ForeignKey('self', related_name='parent', on_delete=models.CASCADE,default='')
    # # 向哪个用户发表的博客评论的
    # reply_to = models.ForeignKey(User, related_name='reply_to_user', on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-comment_time']
