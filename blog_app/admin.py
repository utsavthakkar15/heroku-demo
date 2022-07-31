from django.contrib import admin
from .models import BlogCategory,BlogTags,Blog
# Register your models here.

admin.site.register(BlogCategory)
admin.site.register(BlogTags)
admin.site.register(Blog)