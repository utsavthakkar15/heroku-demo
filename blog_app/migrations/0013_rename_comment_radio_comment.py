# Generated by Django 4.0.6 on 2022-08-02 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_comment_radio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment_radio',
            new_name='Comment',
        ),
    ]
