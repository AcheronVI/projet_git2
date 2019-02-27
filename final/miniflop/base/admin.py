from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from django.contrib import admin

from base.models import Course, Group, Module, Room, RoomType, ModuleDisplay, ScheduledCourse
from people.models import Tutor

# Register your models here.
class ScheduledCourseResource(resources.ModelResource):
    id = fields.Field(column_name='id_course',
                      attribute='course',
                      widget=ForeignKeyWidget(Course, 'id'))
    tutor = fields.Field(column_name='tutor_name',
                         attribute='course__tutor',
                        widget=ForeignKeyWidget(Tutor, 'username'))
    group = fields.Field(column_name='gp_name',
                          attribute='course__group',
                          widget=ForeignKeyWidget(Group, 'name'))
    module = fields.Field(column_name='module',
                          attribute='course__module',
                          widget=ForeignKeyWidget(Module, 'abbrev'))
    room = fields.Field(column_name='room',
                        attribute='room',
                        widget=ForeignKeyWidget(Room, 'name'))
    room_type = fields.Field(column_name='room_type',
                             attribute='course__room_type',
                             widget=ForeignKeyWidget(RoomType, 'name'))
    color_bg = fields.Field(column_name='color_bg',
                            attribute='course__module__display',
                            widget=ForeignKeyWidget(ModuleDisplay, 'color_bg'))
    color_txt = fields.Field(column_name='color_txt',
                             attribute='course__module__display',
                             widget=ForeignKeyWidget(ModuleDisplay, 'color_txt'))
    duration = fields.Field(column_name='duration',
                      attribute='course',
                      widget=ForeignKeyWidget(Course, 'duration'))
    

    class Meta:
        model = ScheduledCourse
        fields = ('id', 'group', 'color_bg', 'color_txt',
                  'module', 'day', 'start_time',
                  'week', 'room', 'tutor', 'room_type', 'duration')
