import pdb
from models.booking import Booking
from models.gymclass import Gymclass
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.member_repository as member_repository

booking_repository.delete_all()
gymclass_repository.delete_all()
member_repository.delete_all()

member_1 = Member("Joan Smith", "1985-05-13", "Core", True)
member_2 = Member("Paul Spencer", "1980-10-24", "Plus", True)
member_3 = Member("Pola Nycz", "1990-04-30", "Plus", True)
member_4 = Member("Piotr Krasinski", "1998-02-04", "Core", False)
member_5 = Member("Susan Wright", "2000-09-18", "Core", False)
member_6 = Member("Alex Fox", "1984-06-21", "Plus", True)

member_repository.save(member_1)
member_repository.save(member_2)
member_repository.save(member_3)
member_repository.save(member_4)
member_repository.save(member_5)
member_repository.save(member_6)

gymclass_1 = Gymclass("Crossfit", "Becky", "2022-06-20", "18:00", 45, 8, True)
gymclass_2 = Gymclass("Kettlebells", "Taylor", "2022-06-23", "19:45", 30, 10, True)
gymclass_3 = Gymclass("Yoga", "Karen", "2022-06-24", "20:00", 60, 12, True)
gymclass_4 = Gymclass("Box Fit", "Andrew", "2022-06-25", "17:45", 30, 6, False)
gymclass_5 = Gymclass("Mobility", "Jacob", "2022-06-20", "19:30", 45, 10, True)

gymclass_repository.save(gymclass_1)
gymclass_repository.save(gymclass_2)
gymclass_repository.save(gymclass_3)
gymclass_repository.save(gymclass_4)
gymclass_repository.save(gymclass_5)

booking_1 = Booking(member_1, gymclass_1)
booking_2 = Booking(member_2, gymclass_1)
booking_3 = Booking(member_2, gymclass_2)
booking_4 = Booking(member_3, gymclass_3)
booking_5 = Booking(member_3, gymclass_5)
booking_6 = Booking(member_6, gymclass_1)
booking_7 = Booking(member_6, gymclass_2)
booking_8 = Booking(member_6, gymclass_5)

booking_repository.save(booking_1)
booking_repository.save(booking_2)
booking_repository.save(booking_3)
booking_repository.save(booking_4)
booking_repository.save(booking_5)
booking_repository.save(booking_6)
booking_repository.save(booking_7)
booking_repository.save(booking_8)

member_repository.select_all()
gymclass_repository.select_all()
booking_repository.select_all()

pdb.set_trace()