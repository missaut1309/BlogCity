# Generated by Django 3.0.8 on 2020-11-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20201111_0442'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['title'], name='blog_post_title_e1c6f7_idx'),
        ),
    ]
