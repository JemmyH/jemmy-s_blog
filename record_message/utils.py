from django.contrib.contenttypes.models import ContentType
from .models import ReadNum, ReadDetail
from django.utils import timezone
from django.db.models import Sum
import datetime


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)  # 获取contenttype中的当前博客类型
    key = "%s_%s_read" % (ct.model, obj.pk)  # cookie格式

    if not request.COOKIES.get(key):
        # 总阅读数 +1
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)  # 创建对象readnum，返回boolean值
        """
        get_or_create:
        Look up an object with the given kwargs, creating one if necessary.
        Return a tuple of (object, created), where created is a boolean
        specifying whether an object was created.
        """

        # 当天阅读数 +1
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()

        readnum.read_num += 1
        readnum.save()
    return key


def get_seven_days_read_data(content_type):  # 用于在主页显示近7天的阅读
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums
