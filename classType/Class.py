class Class:
    def __init__(self, lecture_list, discussion_list, lab_list, quiz_list, class_type, class_num, consecutive):
        self.lecture_list = lecture_list
        self.discussion_list = discussion_list
        self.lab_list = lab_list
        self.quiz_list = quiz_list
        self.class_type = class_type
        self.class_num = class_num
        self.consecutive = consecutive

        # when parsing info from the web page, we can analyze whether the lectures are consecutive or not
        # if not consecutive, input a dict_of_lectures
        # else, dict_of_lectures = null

    def get_name(self):
        return self.class_type + "-" + self.class_num

    def get_lecture_list(self):
        return self.lecture_list

    def get_discussion_list(self):
        return self.discussion_list

    def get_lab_list(self):
        return self.lab_list

    def get_quiz_list(self):
        return self.quiz_list

    def get_solution(self):
        for l in self.lecture_list:
            print(l)
        return

    def sort_based_on_professor(self):
        self.lecture_list.sort(key=lambda x: x.professor.rating, reverse=True)

    def sort_based_on_time(self):
        self.lecture_list.sort(key=lambda x: x.period.start_time, reverse=True)
        for i in self.lecture_list:
            print(i)
        self.discussion_list.sort(key=lambda x: x.period.start_time, reverse=True)
        for i in self.discussion_list:
            print(i)
        self.lab_list.sort(key=lambda x: x.period.start_time, reverse=True)
        for i in self.lab_list:
            print(i)

    def __str__(self):
        s = "Lecture(s):\n\t" + '\n\t'.join(str(x) for x in self.lecture_list)
        s += "\nDiscussion(s):\n\t" + '\n\t'.join(str(x) for x in self.discussion_list)
        s += "\nLab(s):\n\t" + '\n\t'.join(str(x) for x in self.lab_list)
        s += "\nQuiz:\n\t" + '\n\t'.join(str(x) for x in self.quiz_list)
        return s