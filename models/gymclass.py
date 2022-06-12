from unicodedata import name


class Gymclass:
    def __init__(self, class_name, instructor, date, start_time, duration, capacity, active=False, id=None):
        self.class_name = class_name
        self.instructor = instructor
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.capacity = capacity
        self.active=active
        self.id = id
