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
    if 'class1' in request.GET:
        classes.append(request.GET['class1'])
    if 'class2' in request.GET:
        classes.append(request.GET['class2'])
    if 'class3' in request.GET:
        classes.append(request.GET['class3'])
    if 'class4' in request.GET:
        classes.append(request.GET['class4'])
    if 'class5' in request.GET:
        classes.append(request.GET['class5'])
    schedule = main(classes)
    return render(request, 'index.html', schedule)

def aicoach(request):
    request.encoding='utf-8'
    #得分,出手数,命中率,三分出手数,三分命中率,罚球数,罚球命中率
    if 'score' in request.GET and request.GET['score']:
        score = request.GET['score']
    else:
        score = 0
    if 'shots' in request.GET and request.GET['shots']:
        shots = request.GET['shots']
    else:
        shots = 0
    if 'acc' in request.GET and request.GET['acc']:
        acc = request.GET['acc']
    else:
        acc = 0
    if 'threeShots' in request.GET and request.GET['threeShots']:
        threeShots = request.GET['threeShots']
    else:
        threeShots = 0
    if 'threeAcc' in request.GET and request.GET['threeAcc']:
        threeAcc = request.GET['threeAcc']
    else:
        threeAcc = 0
    if 'freeShots' in request.GET and request.GET['freeShots']:
        freeShots = request.GET['freeShots']
    else:
        freeShots = 0
    if 'freeAcc' in request.GET and request.GET['freeAcc']:
        freeAcc = request.GET['freeAcc']
    else:
        freeAcc = 0
    data = [float(score), float(shots), float(acc)/100, float(threeShots), float(threeAcc)/100, float(freeShots), float(freeAcc)/100]
    c= {}
    return render(request, "aicoach.html", c) 
