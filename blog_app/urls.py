from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("about/", views.about, name="about"),
    path('<slug:slug>/category',views.blog_category,name='category'),
    path('<slug:slug>/tag',views.blog_tags,name='tag'),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("<slug:slug>/blogdetail/", views.blogdetail, name="blogdetail"),
    path('<slug:slug>/like',views.video_liked,name='like'),
    path("addblog/", views.add_blog, name="addblog"), 
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)