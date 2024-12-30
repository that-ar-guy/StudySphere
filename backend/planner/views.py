from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject
# Create your views here.
def welcome(request):
    subjects = Subject.objects.all()
    return render(request, 'planner/welcome.html', {'subjects': subjects})
