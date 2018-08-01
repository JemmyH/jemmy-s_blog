from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm


def update_comment(request):
    comment_form = CommentForm(request.POST, user=request.user)
    return_data = {}
    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()
        return_data['status'] = 'SUCCESS'
        return_data['username'] = comment.user.username
        return_data['comment_time'] = comment.comment_time.timestamp()
        return_data['text'] = comment.text
        return_data['content_type'] = ContentType.objects.get_for_model(comment).model
        return_data['pk'] = comment.pk
    else:
        return_data['status'] = 'ERROR'
        return_data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(return_data)
