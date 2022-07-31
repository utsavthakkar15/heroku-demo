from django.contrib import admin
from .models import BlogCategory,BlogTags
# Register your models here.

admin.site.register(BlogCategory)
admin.site.register(BlogTags)