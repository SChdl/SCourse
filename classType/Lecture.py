from classType.Section import Section
class Lecture(Section):
    def __init__(self, section_param, class_name, period_param, registered_param, capacity_param, instructor_param, location_param, color_param):
        super().__init__(section_param, class_name, period_param, registered_param, capacity_param, location_param, color_param)
        self.professor = instructor_param
        self.class_name = class_name

    def get_class_name(self):
        return self.class_name

    def get_professor(self):
        return self.professor

