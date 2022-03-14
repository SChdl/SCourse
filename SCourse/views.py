from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import os
import requests
from main import main

def index(request):
    return render(request, "index.html", {})

def arrange(request):
    classes = []
    prof = False
    t = False
    if 'class1' in request.POST and request.POST['class1'] is not '':
        classes.append(request.POST['class1'])
    if 'class2' in request.POST and request.POST['class2'] is not '':
        classes.append(request.POST['class2'])
    if 'class3' in request.POST and request.POST['class3'] is not '':
        classes.append(request.POST['class3'])
    if 'class4' in request.POST and request.POST['class4'] is not '':
        classes.append(request.POST['class4'])
    if 'class5' in request.POST and request.POST['class5'] is not '':
        classes.append(request.POST['class5'])
    if 'professor' in request.POST:
        prof = True
        print('prof in it')
    if 'time' in request.POST:
        print('time in it')
        t = True
    schedule = main(classes, professor=prof, time=t)


    return render(request, 'index.html', schedule)

