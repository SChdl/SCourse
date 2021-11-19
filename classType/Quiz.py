from classType.Section import Section
class Quiz(Section):
    def __init__(self, section_param, period_param, registered_param, capacity_param, instructor_param, location_param):
        super().__init__(section_param, period_param, registered_param, capacity_param, instructor_param, location_param)
