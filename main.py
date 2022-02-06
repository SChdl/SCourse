from SCourse1 import main1

lec_arr = []
dic_arr = []
quiz_arr = []
def check_conflict(section_list):
    for i in range(len(section_list)):
        for j in range(i+1, len(section_list)):
            p_i = section_list[i].get_period()
            p_j = section_list[j].get_period()
            if p_i.if_collision(p_j):
                return i, j
    return []

def arrange_lecture(lecture_list):
    global lec_arr
    temp_arr = []
    for i in lecture_list:
        if len(i) == 0:
            return
        temp_arr.append(i[0])

    conflicted_classes = check_conflict(temp_arr)
    if len(conflicted_classes) == 0:
        lec_arr.append(temp_arr)
    else:
        # this can definitely be optimized
        for i in conflicted_classes:
            removed = lecture_list[i].pop(0)
            arrange_lecture(lecture_list)
            lecture_list[i].insert(0, removed)

def arrange_discussion(discussion_list):
    global dic_arr
    global lec_arr
    temp_arr = []
    for i in discussion_list:
        if len(i) == 0:
            return
        temp_arr.append(i[0])

    for lec in range(len(lec_arr)):
        conflicted_classes = check_conflict(temp_arr + lec_arr[lec])
        if len(conflicted_classes) == 0:
            dic_arr.append(temp_arr)
        else:
            # this can definitely be optimized
            for i in conflicted_classes:
                if i < len(discussion_list):
                    removed = discussion_list[i].pop(0)
                    arrange_discussion(discussion_list)
                    discussion_list[i].insert(0, removed)

def arrange_quiz(quiz_list):
    global quiz_arr
    quiz_arr = []

def main(classes, professor, time):
    class_list = []
    color = 1
    for i in classes:
        class_list.append(main1(i, color))
        color += 1
        if color >= 5:
            color = 1

    lecture_list = []
    discussion_list = []
    lab_list = []
    quiz_list = []
    for c in class_list:
        if time:
            c.sort_based_on_time()
        if professor:
            c.sort_based_on_professor()

        lecture_list.append(c.get_lecture_list())
        if len(c.get_discussion_list()) != 0:
            discussion_list.append(c.get_discussion_list())
        if len(c.get_lab_list()) != 0:
            lab_list.append(c.get_lab_list())
        if len(c.get_quiz_list()) != 0:
            quiz_list.append(c.get_quiz_list())
    global lec_arr
    lec_arr = []
    arrange_lecture(lecture_list)
    for i in lec_arr:
        print("\nAll lecture arrangement as follow: ")
        for j in i:
            print('\t'+str(j))
    global dic_arr
    dic_arr = []
    arrange_discussion(discussion_list)
    print("\nAll discussion and lab arrangement as follow: ")
    if len(dic_arr) != 0:
        for i in dic_arr[0]:
            print('\t'+str(i))
    else:
        print("no lab or discussion")

    global quiz_arr
    quiz_arr = []
    arrange_quiz(quiz_list)
    print("\nAll quiz arrangement as follow: ")
    if len(quiz_arr) != 0:
        for i in quiz_arr[0]:
            print('\t'+str(i))
    else:
        print("no quiz")

    return_dic = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    lecs_arr = []
    if len(lec_arr) == 0:
        if len(dic_arr) == 0:
            lec_arr = []
        else:
            lecs_arr = dic_arr[0]
    else:
        lecs_arr = lec_arr[0] + dic_arr[0]
    for lec in lecs_arr:
        # print(lec)
        for day in lec.get_period().get_days_list():
            if day == 1:
                return_dic['Monday'].append(lec.get_dic_format())
            elif day == 2:
                return_dic['Tuesday'].append(lec.get_dic_format())
            elif day == 3:
                return_dic['Wednesday'].append(lec.get_dic_format())
            elif day == 4:
                return_dic['Thursday'].append(lec.get_dic_format())
            elif day == 5:
                return_dic['Friday'].append(lec.get_dic_format())
    # print(return_dic)
    return return_dic
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()