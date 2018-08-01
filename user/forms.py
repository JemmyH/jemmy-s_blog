from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class Login_form(forms.Form):
    user_name = forms.CharField(label="用户名",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    pass_word = forms.CharField(label="密码",
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入登录密码'}))

    def clean(self):
        username = self.cleaned_data['user_name']
        password = self.cleaned_data['pass_word']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class RegForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=30, min_length=3,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入3-30位用户名'}))
    email = forms.EmailField(label='邮箱',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}))
    pass_word = forms.CharField(label='密码', min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    pass_word_again = forms.CharField(label='密码', min_length=6,
                                      widget=forms.PasswordInput(
                                          attrs={'class': 'form-control', 'placeholder': '请再次输入密码'}))

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError('用户名已存在!')
        return user_name

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError('邮箱已被注册已存在!')
        return email

    def clean_pass_word_again(self):
        pass_word = self.cleaned_data['pass_word']
        pass_word_again = self.cleaned_data['pass_word_again']
        if pass_word != pass_word_again:
            raise forms.ValidationError('两次输入密码不一致')
        return pass_word_again
