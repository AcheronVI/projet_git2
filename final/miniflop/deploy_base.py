from base.models import Group, RoomType, Room, Module, ModuleDisplay, GroupDisplay, Course, ScheduledCourse, Day
from people.models import Tutor, Student
import json

with open('semaines_6_a_12.json') as json_data:
    data = json.load(json_data)
    D = data[0]
    Courses = data[1]
    Sched_Courses = data[2]

for id_o, o in D["<class 'base.models.Group'>"].items():
   t=Group(id=int(id_o), name=o['name'])
   t.save()

for id_o, o in D["<class 'base.models.RoomType'>"].items():
   t=RoomType(id=int(id_o), name=o['name'])
   t.save()

for id_o, o in D["<class 'base.models.RoomGroup'>"].items():
   t=Room(id=int(id_o), name=o['name'])
   t.save()

for id_o, o in D["<class 'people.models.Tutor'>"].items():
   t=Tutor(id=int(id_o), username=o['username'], status=o['status'], first_name=o['first_name'], last_name=o['last_name'], email=o['email'])
   t.save()

for id_o, o in D["<class 'people.models.Student'>"].items():
   t=Student(id=int(id_o), username=o['username'], first_name=o['first_name'], last_name=o['last_name'], email=o['email'])
   t.save()

for id_o, o in D["<class 'base.models.Module'>"].items():
   try:
       int(o['head_id'])
       t=Module(id=int(id_o), name=o['name'], abbrev=o['abbrev'], head=Tutor.objects.get(id = o['head_id']))
   except:
       t=Module(id=int(id_o), name=o['name'], abbrev=o['abbrev'])
   t.save()

for id_o, o in D["<class 'base.models.ModuleDisplay'>"].items():
   try:
       t=ModuleDisplay(id=int(id_o), color_bg=o['color_bg'], color_txt=o['color_txt'], module=Module.objects.get(id = o['module_id']))
       t.save()
   except:
       print('problem for', o)

for id_o, o in D["<class 'base.models.GroupDisplay'>"].items():
   try:
       t=GroupDisplay(id=int(id_o), button_txt=o['button_txt'], button_height=o['button_height'], group=Group.objects.get(id = o['group_id']))
       t.save()
   except:
       print('problem for', o)


for id_c, c in Courses.items():
    t=Course(id=int(id_c), week=c['week'], year=c['year'], tutor=Tutor.objects.get(id=c['tutor_id']), group=Group.objects.get(id=c['group_id']), module=Module.objects.get(id=c['module_id']), duration=90)
    t.save()

Days = [d for d in Day]
st = [8,9.5,11,14.25, 15.75, 17.25]
for id_sc, sc in Sched_Courses.items():
    t=ScheduledCourse(id=int(id_sc), course=Course.objects.get(id = sc['course_id']),  room=Room.objects.get(id=sc['room_id']))
    creneau = D["<class 'base.models.Slot'>"][str(sc['creneau_id'])]
    t.day=Days[creneau['jour_id']-1].value
    t.start_time=st[creneau['heure_id']-1]*60
    t.save()

