# Generated by Django 4.0.6 on 2022-07-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_blog_created_at_blog_is_active_blog_modify_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_category',
            field=models.ManyToManyField(blank=True, default='', related_name='blogcateg', to='blog_app.blogcategory'),
        ),
    ]
