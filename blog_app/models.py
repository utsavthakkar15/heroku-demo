from pyexpat import model
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.


class BlogCategory(models.Model):
    categoty_id=models.AutoField(primary_key=True,unique=True)
    categoty_type=models.CharField(max_length=20)
    category_image=models.ImageField(upload_to='documents/categoryimage/')
    slug=models.SlugField(unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("category",kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.categoty_type
    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super(BlogCategory,self).save(*args,**kwargs)

@receiver(post_save, sender=BlogCategory)
def create_slug(sender, instance, created, **kwargs):
    if created:
            instance.slug=instance.categoty_type
            instance.save()
class BlogTags(models.Model):
    tag_id=models.AutoField(primary_key=True,unique=True)
    tag_name=models.CharField(max_length=100)
    tag_image=models.ImageField(upload_to='documents/tagimage/')
    slug=models.SlugField(unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse("tag",kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.tag_name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super(BlogTags,self).save(*args,**kwargs)

@receiver(post_save, sender=BlogTags)
def create_slug(sender, instance, created, **kwargs):
    if created:
            instance.slug=instance.tag_name
            instance.save()

class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True,unique=True)
    blog_tilte=models.CharField(max_length=100)
    blog_description=RichTextField()
    blog_image=models.ImageField(upload_to='documents/blogimages/')
    blog_tagLine=models.CharField(max_length=500)
    blog_category=models.ManyToManyField(BlogCategory,default='',blank=True,related_name='blogcateg')
    blog_tag=models.ManyToManyField(BlogTags,default='',blank=True)
    blog_tagLine=models.CharField(max_length=500)
    slug=slug=models.SlugField(unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("blogdetail",kwargs={'slug':self.slug})
    

    def __str__(self):
        return self.blog_tilte

    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super(Blog,self).save(*args,**kwargs)

@receiver(post_save, sender=Blog)
def create_slug(sender, instance, created, **kwargs):
    if created:
            instance.slug=instance.blog_tilte
            instance.save()
