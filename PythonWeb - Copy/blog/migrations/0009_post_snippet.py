# Generated by Django 3.1.1 on 2020-11-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201107_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click to link to read post!!', max_length=255),
        ),
    ]
