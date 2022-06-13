import pdb
from models.booking import Booking
from models.gymclass import Gymclass
from models.member import Member
import repositories.booking_repository as booking_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.member_repository as member_repository

#booking_repository.delete_all()
#gymclass_repository.delete_all()
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



pdb.set_trace()