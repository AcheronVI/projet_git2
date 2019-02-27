from django.db import models
from django.core.validators import MaxValueValidator
from enum import Enum


# Create your models here.

class Day(Enum):
	MONDAY = "m"
	TUESDAY = "tu"
	WEDNESDAY = "w"
	THURSDAY = "th"
	FRIDAY = "f"
	SATURDAY = "sa"
	SUNDAY = "su"
	
class Group(models.Model):
	name = models.CharField(max_length=4)
	parent_group = models.ForeignKey('self',
									blank=True,
									null=True,
									related_name="children_group",
									on_delete=models.CASCADE)
	def __str__(self):
		return self.name
		
class RoomType(models.Model):
	name = models.CharField(max_length=5)
	
	def __str__(self):
		return self.name
		
class Room(models.Model):
	name = models.CharField()
	room_type = models.ManyToManyField('RoomType',
								blank=True,
								null=True,
								related_name="room")
class Module(models.Model):
	name = models.CharField()
	abbrev = models.CharField(max_length=10)
	head = models.ForeignKey('Tutor',
								blank=True,
								null=True,
								related_name="head",
								on_delete=models.SET_NULL)
	
class Course(models.Model):
	group = models.ForeignKey('Group',
								blank=True,
								null=True,
								related_name="course",
								on_delete=models.SET_NULL)
	tutor = models.ForeignKey('Tutor',
								blank=True,
								null=True,
								related_name="course",
								on_delete=models.SET_NULL)
	module = models.ForeignKey('Module',
								blank=True,
								null=True,
								related_name="course",
								on_delete=models.SET_NULL)
								
	room_type = models.ForeignKey('RoomType',
								blank=True,
								null=True,
								related_name="course",
								on_delete=models.SET_NULL)
	
	week = PositiveIntegerField(validators=[MaxValueValidator(53)])
	
	year = PositiveIntegerField()
	
	duration = PositiveIntegerField()
		
class ScheduledCourse(models.Model):
	course = models.ForeignKey('Course',
								blank=True,
								null=True,
								related_name="scheduledCourse",
								on_delete=models.SET_NULL)
	day = models.CharField(max_length=2,
						default= Day.MONDAY,
						choices=[(d,d.value) for d in Day])
	start_time = models.PositiveIntegerField()
	
	room = models.ForeignKey('Room',
								blank=True,
								null=True,
								related_name="scheduledCourse",
								on_delete=models.SET_NULL)
								
class ModuleDisplay(models.Model):
	module = models.OneToOneField('Module',
								blank=True,
								null=True,
								related_name="module_display")
	color_bg = models.CharField(min_length=7, max_length=7)
	color_txt = models.CharField(min_length=7, max_length=7)
	
class GroupDisplay(models.Model):
	group = models.ForeignKey('Group',
								blank=True,
								null=True,
								related_name="group_display",
								on_delete=models.SET_NULL)
	
	button_height = models.PositiveSmallIntegerField()
	button_txt = models.CharField(max_length=50)
	


								

					
