from django.shortcuts import render
from registration.models import Course
from registration.models import Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    context = {
        'fathername': 'Aryan Firaz',
        'mothername': 'Rina Zulaikha',
        'greeting' : 1,
    }
    return render (request,'index.html',context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code'] #code sama dengan course.html
        c_desc = request.POST['desc'] #code sama dengan course.html
        data=Course(code=c_code, description=c_desc)  #code dengan description sama dengan models.py
        data.save()
        allcourse = Course.objects.all().values()
        dict ={
            'message':'Data Save',
            'allcourse': allcourse,
        }
    else:
        allcourse = Course.objects.all().values()
        dict = {
            'message':'Data Save',
            'allcourse': allcourse,
        }

    return render (request, 'course.html', dict)

def mentor(request):
    if request.method == 'POST':
        m_code = request.POST['code'] #code sama dengan mentor.html
        m_name = request.POST['name'] #code sama dengan mentor.html
        m_email = request.POST['email']

        data=Mentor(mentorID=m_code, mentorName=m_name, mentorEmail=m_email)  #code dengan description sama dengan models.py
        data.save()
        allmentor = Mentor.objects.all().values()
        context ={
            'message':'Data Save',
            'allmentor': allmentor,
        }
    else:
        allmentor = Mentor.objects.all().values()
        context = {
            'message':'Data Save',
            'allmentor': allmentor,
        }

    return render (request, 'mentor.html', context)

def searchcourse(request):
    if request.method =='GET':
        # Retrieve the c_code parameter and check if it's not None
        c_code = request.GET.get('c_code')

        if c_code:
            #apply .upper() to ensure uppercase comparison
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None
        #use a different name for the context dictionary
        context = {
            'data' : data
        }

        return render(request, "searchcourse.html", context)
    
    #In case of non_GET request (e.g., POST), return an empty template
    return render(request, "searchcourse.html")

def updateCourse(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data
    }
    return render (request, "updateCourse.html", dict)

def save_update_course(request,code):
    c_desc=request.POST['desc']
    data=Course.objects.get(code=code)
    data.desc = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))
