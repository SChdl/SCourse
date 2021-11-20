class Period:
    def __init__(self, time, days):
        # let 00:00 be 0
        # let 10:00 be 600
        # let 12:00 be 720
        # let 24:00 be 1440

        # time is input as a string:
        # 11:00 - 12:20pm
        # 11:00 - 1:20pm
        # 9:00 - 12:20pm
        # 5:00 - 8:50pm
        self.all_periods = []
        self.days_list = []
        self.timeString = time
        self.dayString = days
        time = time.replace(" ", "")
        if time == "TBA" or days == "TBA":
            self.start_time = 0
            self.end_time = 0
        else:
            afternoon = False
            if time[-2:] == 'pm':
                afternoon = True
            time = time.replace("pm", "")
            time = time.replace("am", "")
            start_time_list = time.split('-')[0].split(':')
            end_time_list = time.split('-')[1].split(':')

            if int(start_time_list[0]) <= int(end_time_list[0]):
                self.start_time = int(start_time_list[0])*60 + int(start_time_list[1])
                self.end_time = int(end_time_list[0])*60 + int(end_time_list[1])
                if afternoon and end_time_list[0] != "12":
                    self.start_time += 720
                    self.end_time += 720
            else:
                self.start_time = int(start_time_list[0])*60 + int(start_time_list[1])
                self.end_time = 720 + int(end_time_list[0])*60 + int(end_time_list[1])

            # date_list = a list of string
            # "Mon,Wed"
            # "Thursday"
            # "MWF"
            if days.find('M') != -1:
                self.days_list.append(1)
            if days.find('Tu') != -1:
                self.days_list.append(2)
            if days.find('W') != -1:
                self.days_list.append(3)
            if days.find('Th') != -1:
                self.days_list.append(4)
            if days.find('F') != -1:
                self.days_list.append(5)

            for d in self.days_list:
                self.all_periods.append((int(d), self.start_time, self.end_time))

    def __str__(self):
        s = self.timeString + ' days: ' + self.dayString
        return s

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_start_time_string(self):
        if self.start_time % 60 == 0:
            endString = '00'
        else:
            endString = str(self.start_time % 60)
        return str(int(self.start_time/60)) + ':' + endString

    def get_end_time_string(self):
        if self.end_time % 60 == 0:
            endString = '00'
        else:
            endString = str(self.end_time % 60)
        return str(int(self.end_time/60)) + ':' + endString

    def get_time_string(self):
        return self.timeString

    def get_days_list(self):
        return self.days_list

    def get_all_periods(self):
        return self.all_periods

    def if_same_day(self, days_a, days_b):
        for a in days_a:
            for b in days_b:
                if a == b:
                    return True
        return False

    def if_collision(self, period):
        a_start = self.get_start_time()
        a_end = self.get_end_time()
        a_days = self.get_days_list()
        b_start = period.get_start_time()
        b_end = period.get_end_time()
        b_days = period.get_days_list()
        if b_start <= a_start <= b_end or b_start <= a_end <= b_end:
            if self.if_same_day(a_days, b_days):
                return True
        return False