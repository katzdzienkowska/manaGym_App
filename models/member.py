class Member:
    def __init__(self, name, dob, membership, active=False, id=None):
        self.name = name
        self.dob = dob
        self.membership = membership
        self.active = active
        self.id = id

#think about memberships - where to store the data plus set up default value?