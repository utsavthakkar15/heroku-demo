from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def base(request):
    return render(request,'base.html')


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    return render(request,'contact.html')


def postdetail(request):
    return render(request,'post_details.html')