# Generated by Django 3.1.1 on 2020-11-11 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20201109_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
    ]
