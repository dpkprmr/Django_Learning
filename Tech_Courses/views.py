from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Allcourses
from django.template import loader

# Create your views here.

def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('Tech_Courses/Courses.html')
    context = {
        'ac': ac,
    }
    # return HttpResponse('<h1>This is my Homepage</h1>')
    return HttpResponse(template.render(context, request))


def detail(request, course_id):
    try:
        course = Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExist:
        raise Http404("Course is Not Available")
    return HttpResponse('<h2>These are the Course Details for Course ID:' + str(course_id) + '</h2>')
