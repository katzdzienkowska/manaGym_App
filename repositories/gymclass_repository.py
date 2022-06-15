from db.run_sql import run_sql

from models.gymclass import Gymclass
from models.member import Member


#CRUD: Create, Read, Update and Delete


#Create
def save(gymclass):
    sql = "INSERT INTO gymclasses (gymclass_name, instructor, date, start_time, duration, capacity, active) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [gymclass.gymclass_name, gymclass.instructor, gymclass.date, gymclass.start_time, gymclass.duration, gymclass.capacity, gymclass.active]
    results = run_sql(sql, values)
    gymclass.id = results[0]["id"]
    return gymclass


#Read
def select_all():
    gymclasses = []
    sql = "SELECT * FROM gymclasses"
    results = run_sql(sql)

    for result in results:
        gymclass = Gymclass(result["gymclass_name"], result["instructor"], result["date"], result["start_time"], result["duration"], result["capacity"], result["active"], result["id"])
        gymclasses.append(gymclass)
    return gymclasses


def select(id):
    sql="SELECT * FROM gymclasses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    gymclass = Gymclass(result["gymclass_name"], result["instructor"], result["date"], result["start_time"], result["duration"], result["capacity"], result["active"], result["id"])
    return gymclass


#Update
def update(gymclass):
    sql = "UPDATE gymclasses SET (gymclass_name, instructor, date, start_time, duration, capacity, active) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gymclass.gymclass_name, gymclass.instructor, gymclass.date, gymclass.start_time, gymclass.duration, gymclass.capacity, gymclass.active, gymclass.id]
    run_sql(sql, values)


#Delete
def delete_all():
    sql = "DELETE FROM gymclasses"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM gymclasses WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#members booked
def list_of_members_booked(id):
    members_booked = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.gymclass_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for result in results:
        member = Member(result["name"], result["dob"], result["membership"], result["active"], result["id"])
        members_booked.append(member)
    return members_booked

