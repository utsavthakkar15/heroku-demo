from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("postdetail/", views.postdetail, name="postdetail"), 
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)