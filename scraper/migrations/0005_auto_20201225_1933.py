# Generated by Django 3.1.4 on 2020-12-25 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_auto_20201225_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookposts',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published'),
        ),
    ]
