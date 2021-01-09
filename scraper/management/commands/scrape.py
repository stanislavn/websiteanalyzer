
from facebook_scraper import get_posts
from django.core.management.base import BaseCommand, CommandError
from scraper.models import Website, FacebookPage, FacebookPost
import time
from django.conf import settings
from django.utils.timezone import make_aware


class Command(BaseCommand):
    def handle(self, *args, **options):
        start = time.time()
        facebookpages = FacebookPage.objects.order_by('-pub_date')
        for facebookpage in facebookpages:
            print(facebookpage)
            FacebookPost.facebook_page = facebookpage
            link = facebookpage.link
            try:
                link = link.replace('https://www.facebook.com/', '')
                link = link.replace('https://m.facebook.com/', '')
            except:
                print(link)
                pass
            #try:
            for post in get_posts(link, pages=3, extra_info=True):
                print(post)
                post['facebook_page_id'] = facebookpage.id
                post['time'] = make_aware(post['time'])
                post['fetched_time'] = make_aware(post['fetched_time'])

                for variable in ['like','love','wow','haha','sorry','anger']:
                    try:
                        post[variable] = post['reactions'][variable]
                    except:
                        post[variable] = 0

                p = FacebookPost(**post)
                try:
                    p.save()
                except:
                    print('skipping already existing post {}'.format(post['post_id']))
            #except:
            #    print('Cant retrieve post from page ',link)
        end = time.time()
        elapsed = (end - start)
        self.stdout.write(self.style.SUCCESS('Posts successfully scraped in "%s"' % elapsed))