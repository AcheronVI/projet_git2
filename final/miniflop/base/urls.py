from django.urls import path, re_path

from . import views

app_name = "base"

urlpatterns = [
    path('hello/', views.hello_world, name="hello"),
    re_path(r'^display/(?P<year>[0-9]{4})?',
         views.display,
         name="display"),
    path('fetch_scheduled_courses/<int:year>/',
         views.fetch_courses,
         name="fetch_courses"),
]
