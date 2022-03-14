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
    regex = re.match(r"^[a-zA-z]{4}\-\d{3}[a-z]?$", input)
    if regex:
        return True
    else:
        return False

def arrange(request):
    input = "CSCI-310"
    print(input)
    print(correct_format(input))

    classes = []
    prof = False
    t = False
    invalid_format = False
    if 'class1' in request.POST and request.POST['class1'] is not '':
        if correct_format(request.POST['class1']):
            classes.append(request.POST['class1'])
        else:
            invalid_format = True
    if 'class2' in request.POST and request.POST['class2'] is not '':
        if correct_format(request.POST['class2']):
            classes.append(request.POST['class2'])
        else:
            invalid_format = True
    if 'class3' in request.POST and request.POST['class3'] is not '':
        if correct_format(request.POST['class3']):
            classes.append(request.POST['class3'])
        else:
            invalid_format = True
    if 'class4' in request.POST and request.POST['class4'] is not '':
        if correct_format(request.POST['class4']):
            classes.append(request.POST['class4'])
        else:
            invalid_format = True
    if 'class5' in request.POST and request.POST['class5'] is not '':
        if correct_format(request.POST['class5']):
            classes.append(request.POST['class5'])
        else:
            invalid_format = True
    if 'professor' in request.POST:
        prof = True
        print('prof in it')
    if 'time' in request.POST:
        print('time in it')
        t = True
    schedule = main(classes, professor=prof, time=t)
    schedule['invalid'] = invalid_format

    return render(request, 'index.html', schedule)

