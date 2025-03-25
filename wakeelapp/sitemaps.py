from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blogs

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return [
            'wakeelapp:index',
            'wakeelapp:calculator',
            'wakeelapp:atl',
            'wakeelapp:ntn',
            'wakeelapp:faq',
            'wakeelapp:contact',
            'wakeelapp:blogs',
            'wakeelapp:video',
            'wakeelapp:about',
            'wakeelapp:services',
            'wakeelapp:login',
            'wakeelapp:zakatcalculator',
            'wakeelapp:currencyconvert',
        
        ]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Blogs.objects.all()  # Fetch all blog posts

    def location(self, obj):
        
        return reverse('wakeelapp:blogdetail', kwargs={'blogs_slug': obj.slug})
