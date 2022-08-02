# Generated by Django 4.0.6 on 2022-08-02 15:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0009_blog_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, default='', related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
