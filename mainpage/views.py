from django.shortcuts import render
from teachers.models import Teacher
from subjects.models import Subject
from testimonials.models import Testimonial

# Create your views here.

def show_mainpage(request):
    template_ = 'mainpage.html'
    teachers = Teacher.objects.all()
    testimonials = Testimonial.objects.all()
    subjects = Subject.objects.all()

    context = {
        'teachers': teachers,
        'testimonials': testimonials,
        'subjects': subjects,
    }
    return render(request=request, template_name=template_, context=context)


