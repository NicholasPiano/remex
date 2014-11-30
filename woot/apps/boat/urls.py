#apps.boat.urls

#django
from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView, RedirectView

from .views import *

urlpatterns = patterns('boat.views',
       # (r'^example_url/', 'example_view')
)




