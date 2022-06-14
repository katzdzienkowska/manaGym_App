import unittest
from models.booking import Booking
from models.gymclass import Gymclass
from models.member import Member

class GymTest(unittest.TestCase):
    def setUp(self):
        self.member_1 = Member("Kat Zdzienkowska", "1988-06-04", "Plus", True)
        self.gymclass_1 = Gymclass("Ballet", "Lisa", "2022-06-30", "10:00", 60, 4, True)
        
    def test_member_has_name(self):
       self.assertEqual("Kat Zdzienkowska", self.member_1.name)

    def test_member_is_active(self):
        self.assertEqual(True, self.member_1.active)

    def test_gymclass_has_instructor(self):
        self.assertEqual("Lisa", self.gymclass_1.instructor)

    def test_gymclass_has_capacity(self):
        self.assertEqual(4, self.gymclass_1.capacity)
    