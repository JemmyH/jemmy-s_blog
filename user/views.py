from django.shortcuts import render, redirect
from .forms import Login_form, RegForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse


def login(request):
    if request.method == 'POST':  # POST表示登录
        login_form = Login_form(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = Login_form()
    context = {'login_form': login_form}
    return render(request, 'user/login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            user_name = reg_form.cleaned_data['user_name']
            email = reg_form.cleaned_data['email']
            pass_word = reg_form.cleaned_data['pass_word_again']
            user = User.objects.create_user(user_name, email, pass_word)
            user.save()
            user = auth.authenticate(username=user_name, password=pass_word)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()
    conetxt = {'reg_form': reg_form}
    return render(request, 'user/register.html', context=conetxt)


def user_info(request):
    context = {}
    return render(request, 'user/user_info.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))
