from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.views import serve

# Create your views here.
def hello_world(request):
    return HttpResponse("Salut !")


def display(request, year):
    if year is None:
        year = 0
        
    try:
        year = int(year)
    except ValueError:
        year = 0
        
    return render(request,
                  'base/edt.html',
                  {'yyyy': year})


def fetch_courses(request, year):

    if year not in [2018, 2019]:
        return serve(request,
                     'base/data.csv')

    return serve(request,
                 'base/data' + str(year) + '.csv')
