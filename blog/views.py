from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogType
from django.db.models.aggregates import Count
from django.core.paginator import Paginator
from record_message.utils import read_statistics_once_read


def blog_list(request):
    blogs = Blog.objects.all()
    blog_types = BlogType.objects.annotate(blog_count=Count('blog'))
    paginator = Paginator(blogs, 10)
    page_num = request.GET.get('page', 1)  # 从url的get请求中获取想要读取的页数
    page_of_blogs = paginator.get_page(page_num)  # 根据请求的页数返回该页的文章

    current_page_num = page_of_blogs.number  # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {'blogs': page_of_blogs,
               'blog_types': blog_types,
               'page_range': page_range}
    return render(request, 'blog/blog_list.html', context)


def blog_datail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    cookie_key = read_statistics_once_read(request, blog)
    context = {'blog': blog}
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    response = render(request, 'blog/blog_detail.html', context)  # 响应
    response.set_cookie(cookie_key, 'true')  # 阅读cookie标记
    return response


def blog_type_list(request, blog_type_id):
    blog_typer = get_object_or_404(BlogType, pk=blog_type_id)
    blog_types = BlogType.objects.annotate(blog_count=Count('blog'))
    blogs = Blog.objects.filter(blog_type=blog_typer)
    paginator = Paginator(blogs, 10)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)  # 根据请求的页数返回该页的文章

    current_page_num = page_of_blogs.number  # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {
        'blogs': page_of_blogs,
        'page_range': page_range,
        'blog_type': blog_typer,
        'blog_types': blog_types,
    }
    return render(request, 'blog/blog_type_detail.html', context)
