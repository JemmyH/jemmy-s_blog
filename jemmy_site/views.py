import datetime
from django.shortcuts import render
from django.utils import timezone
from record_message.models import ReadNum, ReadDetail


def get_7_days_hot_blogs():
    # 关于时区问题，数据库使用UTC，而中国使用UTC+8，所以时间相差8个小时，我也懒得去改了……
    today = timezone.now().date()
    date_range = [today]
    date_read_count = []
    for i in range(1, 7):
        date_range.append(today - datetime.timedelta(days=i))
    for d in date_range:
        k = 0
        for n in ReadDetail.objects.filter(date__contains=d):
            k += n.read_num
        date_read_count.append(k)
    return date_range, date_read_count


def home(request):
    dates, read_nums = get_7_days_hot_blogs()
    popular = ReadNum.objects.all().order_by('-read_num')[:7]
    context = {}
    context['dates'] = ["{0}月{1}日".format(i.month, i.day) for i in dates[::-1]]  # z最近7天序列
    context['read_nums'] = read_nums[::-1]  # 每一天的阅读量
    # context['hot_blogs_for_7_days'] = hot_blogs_for_7_days  # 暂时没什么用
    context['most_popular'] = popular
    return render(request, 'mysite_index.html', context)


def contact_me(request):
    return render(request, 'contact_me.html')


def index(request):
    return render(request, "index.html")


def netease(request):
    return render(request, 'netease/netease_index.html')


def luoo(request):
    return render(request, 'luoo/luoo_index.html')


def xiaohaitun(request):
    return render(request, 'xiaohaitun.html')


def pintu(request):
    return render(request, 'pintu.html')


def iframe(request):
    return render(request, 'demo.html')
