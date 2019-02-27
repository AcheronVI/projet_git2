from django.db import models
from django.contrib.auth.models import User
from base.models import *

# Create your models here.

class Tutor(User):
	
class FullStaff(models.Tutor):
	
class FullStaff(models.Tutor):
	employer = models.CharField()
	position = models.IntegerField()
	
class Student():
	belong_to = models.OneToManyField('Group',
								blank=True,
								null=True,
								related_name="module_display",
								on_delete=models.SET_NULL)
