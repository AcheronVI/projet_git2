from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.views import serve

# Create your views here.
def hello(request):
	return HttpResponse("popiopopopipo")

def display(request, annee):
    dataC='base/data'+str(annee)+'.csv'
    return render(request, 'base/edt.html', {'dataC':dataC})
	


def fetch_scheduled_courses(request, annee):
    if annee==2019:
    	return serve(request, 'base/data_2019.csv', {})
    elif annee==2018:
        return serve(request, 'base/data_2018.csv', {})
    else:
        return serve(request, 'base/data.csv', {})