from pyexpat import model
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class BlogCategory(models.Model):
    categoty_id=models.AutoField(primary_key=True,unique=True)
    categoty_type=models.CharField(max_length=20)
    category_image=models.ImageField(upload_to='documents/categoryimage/')
    slug=models.SlugField(unique=True,default=categoty_type)
    
    def get_absolute_url(self):
        return reverse("category",kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.categoty_type
    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super(BlogCategory,self).save(*args,**kwargs)

class BlogTags(models.Model):
    tag_id=models.AutoField(primary_key=True,unique=True)
    tag_name=models.CharField(max_length=100)
    tag_image=models.ImageField(upload_to='documents/tagimage/')
    slug=models.SlugField(unique=True,default=tag_name)

    def get_absolute_url(self):
        return reverse("tag",kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.tag_name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super(BlogTags,self).save(*args,**kwargs)




