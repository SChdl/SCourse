import os
from bs4 import BeautifulSoup as bs
import urllib.request
import ssl
import json

from classType import *

def store_webpage(url, ctx, fn):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urllib.request.urlopen(req, context=ctx)
    soup = bs(page.read(), 'html.parser')
    f = open(fn, 'w')
    print(soup, file=f)
    f.close()

def load_webpage(file_name, ctx):
    page = urllib.request.urlopen(file_name, context=ctx)
    return bs(page.read(), 'html.parser')

def main1(input_, color):
    course_name = input_
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    if os.path.exists('sites/' + course_name + '.html'):
        print("this course is already loaded")
    else:
        store_webpage('https://classes.usc.edu/term-20231/course/' + course_name, ctx, 'sites/' + course_name + '.html')

    class_file_name = 'file://' + os.getcwd() + '/sites/' + course_name + '.html'
    soup_class = load_webpage(class_file_name, ctx)
    class_section = soup_class.find_all('td', class_="section")
    class_type = soup_class.find_all('td', class_="type")
    class_time = soup_class.find_all('td', class_="time")
    class_days = soup_class.find_all('td', class_="days")
    class_registered = soup_class.find_all('td', class_="registered")
    class_instructor = soup_class.find_all('td', class_="instructor")
    class_location = soup_class.find_all('td', class_="location")
    lecture_list = []
    discussion_list = []
    lab_list = []
    quiz_list = []
    if course_name == "":
        return
    class_category = course_name.split('-')[0]
    class_num = course_name.split('-')[1]
    consecutive_flag = False
    consecutive = True
    with open('ratings.json') as json_file:
        ratings = json.load(json_file)
    for i in range(len(class_section)):
        if 'Lecture' in class_type[i].text:
            if consecutive_flag:
                consecutive = False
            if ratings.get(class_instructor[i].text):
                lecture_list.append(Lecture(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text), int(class_registered[i].text.split()[0]), int(class_registered[i].text.split()[2]), Professor(class_instructor[i].text, ratings[class_instructor[i].text]['rating']), class_location[i].text, color))
            else:
                lecture_list.append(
                    Lecture(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text),
                            int(class_registered[i].text.split()[0]), int(class_registered[i].text.split()[2]),
                            Professor(class_instructor[i].text, 0),
                            class_location[i].text, color))

            consecutive_flag = True
        elif class_type[i].text == 'Discussion':
            discussion_list.append(Discussion(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text), int(class_registered[i].text.split()[0]), int(class_registered[i].text.split()[2]), class_location[i].text, color))
            consecutive_flag = False
        elif class_type[i].text == 'Lab':
            if class_registered[i].text == 'Canceled':
                discussion_list.append(
                    Lab(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text),
                        0, 0,
                        class_location[i].text, color))
            else:
                discussion_list.append(Lab(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text), int(class_registered[i].text.split()[0]), int(class_registered[i].text.split()[2]), class_location[i].text, color))
            consecutive_flag = False
        elif class_type[i].text == 'Quiz':
            quiz_list.append(Quiz(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text), int(class_registered[i].text.split()[0]), int(class_registered[i].text.split()[2]), class_location[i].text, color))
            consecutive_flag = False
        elif class_type[i].text == '':
            lecture_list[-1].add_period(Period(class_time[i].text, class_days[i].text))
            print(lecture_list[-1])
        else:
            print(class_type[i].text)
            if consecutive_flag:
                consecutive = False
            if ratings.get(class_instructor[i].text):
                lecture_list.append(Lecture(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text), int(class_registered[i].text.split()[0]), int(class_registered[i].text.split()[2]), Professor(class_instructor[i].text, ratings[class_instructor[i].text]['rating']), class_location[i].text, color))
            else:
                lecture_list.append(
                    Lecture(class_section[i].text, input_, Period(class_time[i].text, class_days[i].text),
                            int(class_registered[i].text.split()[0]), int(class_registered[i].text.split()[2]),
                            Professor(class_instructor[i].text, 0),
                            class_location[i].text, color))
            consecutive_flag = True
    c = Class(lecture_list, discussion_list, lab_list, quiz_list, class_category, class_num, consecutive)
    print(c)
    return c

if __name__ == '__main__':
    main1()