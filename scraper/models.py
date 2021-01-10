from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

# class Website(models.Model):
#     name = models.TextField(max_length=200, unique=True)
#     link = models.TextField(max_length=200, unique=True)
#     description = models.TextField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.name
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class FacebookPage(models.Model):
    name = models.TextField(max_length=200, unique=True)
    link = models.TextField(max_length=200, unique=True)
    description = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class FacebookPost(models.Model):
    facebook_page   = models.ForeignKey(FacebookPage, on_delete=models.CASCADE)
    post_id         = models.BigIntegerField(unique=True)
    text            = models.TextField(max_length=900, blank = True, null=True)
    post_text       = models.TextField(max_length=900, blank = True, null=True)
    shared_text     = models.TextField(blank = True, null=True)
    time            = models.DateTimeField('date published', blank = True, null=True)
    scrape_time     = models.DateTimeField('date scraped', blank=True, null=True, auto_now_add=True)
    fetched_time    = models.DateTimeField('date scraped', blank=True, null=True)
    image           = models.URLField(max_length=900, blank = True, null=True)
    video           = models.URLField(max_length=900, blank = True, null=True)
    video_thumbnail = models.URLField(max_length=900, blank = True, null=True)
    video_id        = models.BigIntegerField(blank = True, null=True)
    likes           = models.IntegerField(blank = True, null=True)
    like            = models.IntegerField(blank=True, null=True)
    love            = models.IntegerField(blank=True, null=True)
    wow             = models.IntegerField(blank=True, null=True)
    haha            = models.IntegerField(blank=True, null=True)
    sorry           = models.IntegerField(blank=True, null=True)
    anger           = models.IntegerField(blank=True, null=True)
    comments        = models.IntegerField(blank = True, null=True)
    shares          = models.IntegerField(blank = True, null=True)
    post_url        = models.URLField(max_length=900, blank = True, null=True)
    link            = models.URLField(max_length=900, blank = True, null=True)
    user_id         = models.BigIntegerField(blank = True, null=True)
    images          = models.URLField(max_length=900, blank = True, null=True)
    manual_description = models.TextField(max_length=900, blank=True, null=True)
    nlp_description     = models.TextField(max_length=900, blank=True, null=True)
    reactions       = models.TextField(max_length=900, blank=True, null=True)
    w3_fb_url       =  models.URLField(max_length=900, blank = True, null=True)

    def __str__(self):
        return str(self.text[0:120])




#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)