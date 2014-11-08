#apps.club.models

#django
from django.db import models

#local
from apps.user.models import User

#util
import datetime

### Models

#1. Club
class Club(models.Model):
  #connections


  #properties


  #methods


#2. Member
class Member(User):
  #connections


  #properties


  #methods

class Coach(Member):
  #connections


  #properties


  #methods

class Coxswain(Member):
  #connections


  #properties


  #methods

class Remex(Member):
  #connections


  #properties


  #methods


#3. Boat
class Boat(models.Model):
  #connections


  #properties


  #methods
