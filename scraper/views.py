from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Website, FacebookPage

import requests
import json
from celery.schedules import crontab





def index(request):
    websites = Website.objects.order_by('-pub_date')[:5]
    facebookpages = FacebookPage.objects.order_by('-pub_date')[:5]
    context = {'websites': websites, 'facebookpages':facebookpages}
    return render(request, 'scraper/index.html', context)

def scraper(request):
    app_id = '376001406988541'
    app_secret = '4a358a5317e5723834fe0ea288c1168a'
    access_token = app_id + ' | ' + app_secret
    page_id = "time"


    print(fbPageData(page_id, access_token()))

    #websites = Website.objects.order_by('-pub_date')[:5]
    #facebookpages = FacebookPage.objects.order_by('-pub_date')[:5]
    #context = {a: 'a'}
    return render(request, 'scraper/scraper.html', context=None)