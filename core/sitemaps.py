from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Event

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'events', 'gallery', 'contact']

    def location(self, item):
        return reverse(item)

class EventSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Event.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at
