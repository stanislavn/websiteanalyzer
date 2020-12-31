from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class Website(models.Model):
    name = models.TextField(max_length=200, unique=True)
    link = models.TextField(max_length=200, unique=True)
    description = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

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
    text            = models.TextField(blank = True, null=True)
    post_text       = models.TextField(blank = True, null=True)
    shared_text     = models.TextField(blank = True, null=True)
    time            = models.DateTimeField('date published', blank = True, null=True, auto_now_add=True)
    image           = models.URLField(blank = True, null=True)
    video           = models.URLField(blank = True, null=True)
    video_thumbnail = models.URLField(blank = True, null=True)
    video_id        = models.BigIntegerField(blank = True, null=True)
    likes           = models.IntegerField(blank = True, null=True)
    comments        = models.IntegerField(blank = True, null=True)
    shares          = models.IntegerField(blank = True, null=True)
    post_url        = models.URLField(blank = True, null=True)
    link            = models.URLField(blank = True, null=True)
    user_id         = models.BigIntegerField(blank = True, null=True)
    images          = models.URLField(blank = True, null=True)
    manual_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.text[0:120])




#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)