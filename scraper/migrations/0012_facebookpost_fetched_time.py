# Generated by Django 3.1.4 on 2021-01-06 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0011_facebookpost_w3_fb_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookpost',
            name='fetched_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date scraped'),
        ),
    ]