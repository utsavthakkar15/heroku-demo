from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


from blog_app.models import Blog, BlogCategory, BlogTags
from .forms import CreateUserForm

# Create your views here.

def base(request):
    return render(request,'base.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                # login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    blog_category_display=BlogCategory.objects.all().order_by('-categoty_id')
    blog_tag_display=BlogTags.objects.all().order_by('-tag_id')
    blogs=Blog.objects.all().values('blog_category__categoty_type','blog_image','blog_tilte','created_at','slug')
    context={
        'blog_category_display':blog_category_display,
        'blog_tag_display':blog_tag_display,
        'blog':blogs,
    }
    
    return render(request,'index.html',context)

def blog_category(request,slug):
    blog_category=BlogCategory.objects.get(slug=slug)
    context={
        'blog_category':blog_category
    }
    return render(request,'base.html',context)
def blog_tags(request,slug):
    blog_tags=BlogTags.objects.get(slug=slug)
    context={
        'blog_tag':blog_tags
    }
    return render(request,'base.html',context)
def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    return render(request,'contact.html')


def blogdetail(request,slug):
    blog=get_object_or_404(Blog,slug=slug)
    
    context={
        'blog':blog,
        
        
    }
    
    return render(request,'post_details.html',context)