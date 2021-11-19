class Section:
    def __init__(self, section_param, period_param, registered_param, capacity_param, instructor_param, location_param):
        self.section = section_param
        self.period = period_param
        self.registered = registered_param
        self.capacity = capacity_param
        self.instructor = instructor_param
        self.location = location_param

    def get_section(self):
        return self.section

    def get_period(self):
        return self.period

    def get_registered(self):
        return self.registered

    def get_capacity(self):
        return self.capacity

    def get_instructor(self):
        return self.instructor

    def get_location(self):
        return self.location

    def get_dic_format(self):
        dic = {"name": self.section, "startTime": self.period.get_start_time_string(), "endTime": self.period.get_end_time_string(), "location": self.location, "instructor": self.instructor}
        return dic

    def __str__(self):
        s = ' '.join([self.section, str(self.period), str(self.registered), str(self.capacity), self.instructor, self.location])
        return s