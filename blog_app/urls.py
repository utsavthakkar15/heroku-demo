from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


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
    path("addblog/", views.add_blog, name="addblog"), 
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)