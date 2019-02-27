from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Tutor(django.contrib.auth.models.User)

class Day(enum):
    MONDAY="m"
    TUESDAY="tu"
    WEDNESDAY="w"
    THURSDAY="th"
    FRIDAY="f"
    SATURDAY="sa"
    SUNDAY="su"

class Group(models.Model):
    name=models.CharField(max_length=4)
    parent_group=models.ForeignKey('self',blank=True,null=True,related_name="children_group",on_delete=models.CASCADE)

class RoomType(models.Model):
    name=models.CharField()

class Room(models.Model):
    name=models.CharField()
    room_type=models.ManyToManyField('RoomType', related_name="room", on_delete=models.SET_NULL)

class Module(models.Model):
    name=models.CharField()
    abbrev=models.CharField(max_length=10)
    head=models.ForeignKey('Tutor',related_name="head", on_delete=models.SET_NULL)

class Course(models.Model):
    groupe=models.ForeignKey('Group',related_name="groupe", on_delete=models.SET_NULL)
    tutor=models.ForeignKey('Tutor',related_name="tutor", on_delete=models.SET_NULL)
    module=models.ForeignKey('Module',related_name="module", on_delete=models.SET_NULL)
    room_type=models.ForeignKey('RoomType', related_name="room_type", on_delete=models.SET_NULL)
    week=models.PositiveIntegerField(validators=[MaxValueValidator(53)])
    year=models.PositiveIntegerField()
    duration=models.PositiveIntegerField()

class ScheduledCourse(models.Model):
    course=models.ForeignKey('Course',related_name="course", on_delete=models.SET_NULL)
    day=models.CharField(max_length=2,default=Day.MONDAY,choices=[(d,d.value)for d in Day])
    start_time=models.PositiveIntegerField()
    room=models.ForeignKey('Room', related_name="room", on_delete=models.SET_NULL)

class ModuleDisplay(models.Model):
    module=models.OneToOneField('Module',related_name="module", on_delete=models.SET_NULL)
    color_bg=models.CharField(min_length=7,max_length=7)
    color_text=models.CharField(min_length=7,max_length=7)

class GroupDisplay(models.Model):
    group=models.OneToOneField('Group',related_name="groupe", on_delete=models.SET_NULL)
    button_height=
    button_txt=


class FullStaff(models.Tutor)

class SupplyStaff (models.Tutor):
    employer=
    position=

class Student (models.Model):
    belong_to=models.OneToMany('Group',related_name="groupe", on_delete=models.SET_NULL)




    