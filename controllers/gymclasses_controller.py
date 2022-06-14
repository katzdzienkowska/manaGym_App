from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.gymclass import Gymclass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("gymclasses", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/xxx'
@gymclasses_blueprint.route("/gymclasses")
def gymclasses():
    all_gymclasses = gymclass_repository.select_all()
    return render_template("gymclasses/index.html", gymclasses=all_gymclasses, title="Gym Classes")

# NEW
# GET '/xxx/new'
@gymclasses_blueprint.route("/gymclasses/new", methods = ["get"])
def new_gymclass():
    return render_template("gymclasses/new.html", title="Add Gym Class")

# CREATE
# POST '/xxx'
@gymclasses_blueprint.route("/gymclasses", methods = ["post"])
def create_gymclass():
    gymclass_name = request.form["gymclass_name"]
    instructor = request.form["instructor"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    active = request.form["active"]
    gymclass = Gymclass(gymclass_name, instructor, date, start_time, duration, capacity, active)
    gymclass_repository.save(gymclass)
    return redirect("/gymclasses")

# SHOW
# GET '/xxx/<id>'
@gymclasses_blueprint.route("/gymclasses/<id>")
def show_gymclass(id):
    booked_members = gymclass_repository.list_of_members_booked(id)
    found_gymclass = gymclass_repository.select(id)
    return render_template("gymclasses/show.html", gymclass=found_gymclass, booked_members=booked_members, title="Gym Class")

# EDIT
# GET '/xxx/<id>/edit'
@gymclasses_blueprint.route("/gymclasses/<id>/edit", methods=["get"])
def edit_gymclass(id):
    edit_gymclass = gymclass_repository.select(id)
    return render_template("gymclasses/edit.html", gymclass=edit_gymclass, title="Edit Gym Class")

# UPDATE
# PUT '/xxx/<id>'
@gymclasses_blueprint.route("/gymclasses/<id>", methods=["post"])
def update_gymclass(id):
    gymclass_name = request.form["gymclass_name"]
    instructor = request.form["instructor"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    active = request.form["active"]
    gymclass = Gymclass(gymclass_name, instructor, date, start_time, duration, capacity, active, id)
    gymclass_repository.update(gymclass)
    return redirect("/gymclasses")

# DELETE
# DELETE '/xxx/<id>'
@gymclasses_blueprint.route("/gymclasses/<id>/delete", methods=["post"])
def delete_gymclass(id):
    gymclass_repository.delete(id)
    return redirect("/gymclasses")