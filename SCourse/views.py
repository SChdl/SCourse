import re

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import os
import requests
from main import main

def index(request):
    return render(request, "index.html", {})

def correct_format(input):
    regex = re.match(r"^[a-zA-z]{2,4}\-\d{3}[a-z]?$", input)
    if regex:
        return True
    else:
        return False

def arrange(request):

    classes = []
    prof = False
    t = False
    invalid_format = False
    if 'class1' in request.POST and request.POST['class1'] != '':
        if correct_format(request.POST['class1']):
            classes.append(request.POST['class1'])
        else:
            invalid_format = True
    if 'class2' in request.POST and request.POST['class2'] != '':
        if correct_format(request.POST['class2']):
            classes.append(request.POST['class2'])
        else:
            invalid_format = True
    if 'class3' in request.POST and request.POST['class3'] != '':
        if correct_format(request.POST['class3']):
            classes.append(request.POST['class3'])
        else:
            invalid_format = True
    if 'class4' in request.POST and request.POST['class4'] != '':
        if correct_format(request.POST['class4']):
            classes.append(request.POST['class4'])
        else:
            invalid_format = True
    if 'class5' in request.POST and request.POST['class5'] != '':
        if correct_format(request.POST['class5']):
            classes.append(request.POST['class5'])
        else:
            invalid_format = True
    if 'class5' in request.POST and request.POST['class6'] != '':
        if correct_format(request.POST['class6']):
            classes.append(request.POST['class6'])
        else:
            invalid_format = True
    if 'professor' in request.POST:
        prof = True
    if 'time' in request.POST:
        t = True
    schedule = main(classes, professor=prof, time=t)
    schedule['invalid'] = invalid_format
    schedule['classOne'] = request.POST['class1']
    schedule['classTwo'] = request.POST['class2']
    schedule['classThree'] = request.POST['class3']
    schedule['classFour'] = request.POST['class4']
    schedule['classFive'] = request.POST['class5']
    schedule['classSix'] = request.POST['class6']
    schedule['professor'] = 'checked' if prof else ''
    schedule['time'] = 'checked' if t else ''
    return render(request, 'index.html', schedule)

