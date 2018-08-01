from django.shortcuts import render, HttpResponse
import requests
import json


# Create your views here.
def netease_index(request):
    return render(request, 'netease/netease_index.html')


def neteaseresearch(request):
    url = request.GET.get('url')
    id = url.split("=")[-1]
    print('http://music.163.com/song/media/outer/url?id={0}.mp3'.format(id))
    return HttpResponse(json.dumps('http://music.163.com/song/media/outer/url?id={0}.mp3'.format(id)))
