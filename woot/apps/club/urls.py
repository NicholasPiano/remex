#apps.club.urls

#django
from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView, RedirectView

from .views import *

urlpatterns = patterns('club.views',
       # (r'^example_url/', 'example_view')
)




