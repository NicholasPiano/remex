#apps.club.models

#django
from django.db import models

#local
from apps.link.models import Link

#util
import datetime

### Models

#1. Club
class Club(models.Model):
  #connections
  #what is a club a part of? A league? A university?
  #St. Edmund's and First and Third are both Cambridge rowing clubs
  #Invesigate multiple database support for cross-site requests
  link = models.ForeignKey(Link, related_name='clubs')

  #properties
  name = models.CharField(max_length=255)

  #methods
