class Member:
    def __init__(self, name, dob="", membership="Core", active=False, id=None):
        self.name = name
        self.dob = dob
        self.membership = membership
        self.active = active
        self.id = id