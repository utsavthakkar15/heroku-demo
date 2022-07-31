from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Blog

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password' )


class AddBlog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('blog_tilte','blog_description','blog_image','blog_tagLine','blog_category','blog_tag','slug')
