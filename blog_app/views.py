from multiprocessing import context
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
    HttpResponseRedirect,
    reverse,
)
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from django.http import HttpResponse
from django.contrib.auth import authenticate, login as dj_login
from blog_app.models import Blog, BlogCategory, BlogTags, Comment
from .forms import CommentForm, ContactusForm, CreateUserForm, AddBlog
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.


def base(request):
    return render(request, "base.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                dj_login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
            return redirect("login")
    else:
        form = CreateUserForm()
    return render(request, "signup.html", {"form": form})


def index(request):
    blog_category_display = BlogCategory.objects.all().order_by("-categoty_id")
    blog_tag_display = BlogTags.objects.all().order_by("-tag_id")
    page = request.GET.get('page',1)
    blogs = (
        Blog.objects.all()
        .values(
            "blog_category__categoty_type",
            "blog_image",
            "blog_tilte",
            "created_at",
            "created_by__username",
            "slug",
            "blog_tag__tag_name",
        )
        .order_by("-blog_id")
    )
    paginator = Paginator(blogs, 4)

    try:

        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)


    context = {
        "blog_category_display": blog_category_display,
        "blog_tag_display": blog_tag_display,
        "blog": blogs,
        'paginate':blogs,
    }

    return render(request, "index.html", context)


def blog_category(request, slug):
    blog_category = BlogCategory.objects.get(slug=slug)
    blog=Blog.objects.filter(blog_category=blog_category)
    print(blog)
    context = {"blog_category": blog_category,'blog':blog}
    return render(request, "see_all_category.html", context)


def blog_tags(request, slug):
    blog_tags = BlogTags.objects.get(slug=slug)
    blog=Blog.objects.filter(blog_tag=blog_tags)
    context = {"blog_tag": blog_tags,"blog":blog}

    return render(request, "see_all_tag.html", context)


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    if request.method=='POST':
        form=ContactusForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactusForm()
    return render(request, "contact.html", {'form':form})
    
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def blogdetail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=blog)
    print(comments)
    is_liked = False
    is_dislike = False
    if blog.likes.filter(id=request.user.id).exists():
        is_liked = True
    if blog.dislike.filter(id=request.user.id).exists():

        is_dislike = True
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet

            # Assign the current post to the comment
            comment_form.instance.blog = blog
            # Save the comment to the database
            comment_form.save()
    else:
        comment_form = CommentForm()
    context = {
        "is_dislike":is_dislike,
        "is_liked":is_liked,
        "blog": blog,
        "comment_form":comment_form,
        "comments":comments,
    }
    if is_ajax(request=request):
        html = render_to_string('comment.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, "post_details.html", context)
@login_required
def video_liked(request,slug):

    blog=get_object_or_404(Blog,slug=slug)
    is_liked=False
    is_dislike = False
    
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        blog.dislike.add(request.user)
        is_dislike = True
        is_liked = False

        
        is_liked = False
    else:
        blog.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(blog.get_absolute_url())

def add_blog(request):
    context = {}
    user = request.user
    form = AddBlog(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.created_by=user
        form.save()
    context["form"] = form
    return render(request, "addblog.html", context)
