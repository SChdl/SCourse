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
    if 'class1' in request.POST:
        classes.append(request.POST['class1'])
    if 'class2' in request.POST:
        classes.append(request.POST['class2'])
    if 'class3' in request.POST:
        classes.append(request.POST['class3'])
    if 'class4' in request.POST:
        classes.append(request.POST['class4'])
    if 'class5' in request.POST:
        classes.append(request.POST['class5'])
    schedule = main(classes)
    return render(request, 'index.html', schedule)