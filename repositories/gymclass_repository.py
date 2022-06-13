from db.run_sql import run_sql

from models.gymclass import Gymclass

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

#added below for future use
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