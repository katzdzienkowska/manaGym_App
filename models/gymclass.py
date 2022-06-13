from unicodedata import name


class Gymclass:
    def __init__(self, gymclass_name, instructor, date, start_time, duration, capacity, active=False, id=None):
        self.gymclass_name = gymclass_name
        self.instructor = instructor
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.capacity = capacity
        self.active=active
        self.id = id
