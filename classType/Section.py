class Section:
    def __init__(self, section_param, class_name, period_param, registered_param, capacity_param, location_param, color_param):
        self.section = section_param
        self.class_name = class_name
        self.period = period_param
        self.registered = registered_param
        self.capacity = capacity_param
        self.location = location_param
        self.color = 'event-' + str(color_param)

    def get_section(self):
        return self.section

    def get_period(self):
        return self.period

    def get_registered(self):
        return self.registered

    def get_capacity(self):
        return self.capacity

    def get_location(self):
        return self.location

    def get_dic_format(self):
        dic = {"name": self.class_name, "section": self.section, "startTime": self.period.get_start_time_string(), "endTime": self.period.get_end_time_string(), "location": self.location, "color": self.color}
        return dic

    def __str__(self):
        s = ' '.join([self.class_name, self.section, str(self.period), str(self.registered), str(self.capacity), self.location])
        return s