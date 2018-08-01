from django.shortcuts import render, HttpResponse
import requests
from lxml import etree
import json


def luoo_index(request):
    return render(request, 'luoo/luoo_index.html')


def search_luowang(request):
    url = request.GET.get('url')
    urls = []
    data = []
    res = etree.HTML(requests.get(url).text)
    names = res.xpath("//*[@id='luooPlayerPlaylist']/ul//li/div[1]/a[1]/text()")
    num = int(res.xpath("//h1[@class='vol-name']/span[1]/text()")[0])
    for i in range(1, len(names) + 1):
        if i < 10:
            index = "0" + str(i)
        else:
            index = str(i)
        urls.append("http://mp3-cdn2.luoo.net/low/luoo/radio{0}/{1}.mp3".format(str(num), index))
    for i, j in zip(names, urls):
        data.append([i,j])
    return HttpResponse(json.dumps(data))

def test(request):
    return HttpResponse("test")
