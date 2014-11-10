#apps.club.models

#django
from django.db import models

#local
from apps.users.models import User

#util
import datetime

### Models

#1. Club
class Club(models.Model):
  #connections


  #properties
  name = models.CharField(max_length=255)

  #methods


#2. Member
class Member(User):
  #connections
  club = models.ForeignKey(Club, related_name='members')

  #properties



  #methods

class Coach(Member):
  #connections


  #properties


  #methods

class Trainer(Member):
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


#4. Events
class Event(models.Model):
  #connections


  #properties


  #methods

class Outing(Event):
  #connections


  #properties


  #methods

class Race(Event):
  #connections


  #properties


  #methods

class Training(Event):
  #connections


  #properties


  #methods
