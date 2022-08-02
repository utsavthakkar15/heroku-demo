from django.contrib import admin
from .models import BlogCategory,BlogTags,Blog,Comment, ContactUs
# Register your models here.

admin.site.register(BlogCategory)
admin.site.register(BlogTags)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(ContactUs)