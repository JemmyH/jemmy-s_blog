from django.shortcuts import render, HttpResponse
import requests
import json
import urllib


# Create your views here.
def echo_index(request):
    return render(request, 'echo/echo_index.html')


def echo_name_index(request):
    return render(request, 'echo/echo_by_name.html')


def parse_song(request):
    url = request.GET.get('url')
    id = url.split("/")[-1]
    if url.find("sound") > -1:
        res = requests.get("http://www.app-echo.com/api/sound/info?id={0}".format(id))
        mp3_url = json.loads(res.text)['info']['source'].split("?")[0]
        name = json.loads(res.text)['info']['name']
    elif url.find("mv") > -1:
        res = requests.get("http://www.app-echo.com/api/mv/info?id={0}".format(id))
        mp3_url = json.loads(res.text)['info']['source'].split("?")[0]
        name = json.loads(res.text)['info']['name']
    result = [mp3_url, name]
    return HttpResponse(json.dumps(result))


def search_song(request):
    key_world = request.GET.get('key_word')
    data = []
    k = 1
    while True:
        value = {'keyword': key_world,
                 'page': str(k),
                 'limit': '10'}
        res = requests.get("http://www.app-echo.com/api/search/sound?{0}".format(urllib.parse.urlencode(value)))
        for i in json.loads(res.text)['data']:
            data.append([i['name'], i['source']])
        if len(json.loads(res.text)['data']) < 10:
            break
        else:
            k += 1
    return HttpResponse(json.dumps(data))
