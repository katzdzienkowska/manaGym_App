from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/xxx'
@bookings_blueprint.route("/bookings")
def bookings():
    all_bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=all_bookings)

# NEW
# GET '/xxx/new'
@bookings_blueprint.route("/bookings/new", methods = ["get"])
def new_booking():
    members = member_repository.select_all()
    gymclasses = gymclass_repository.select_all()
    return render_template("bookings/new.html", members=members, gymclasses=gymclasses) #add title later

# CREATE
# POST '/xxx'
@bookings_blueprint.route("/bookings", methods = ["post"])
def create_booking():
    member_id = request.form["member_id"]
    gymclass_id = request.form["gymclass_id"]
    member = member_repository.select(member_id)
    gymclass = gymclass_repository.select(gymclass_id)
    new_booking = Booking(member, gymclass)
    booking_repository.save(new_booking)
    return redirect("/bookings")

# SHOW
# GET '/xxx/<id>' - not needed here!

# EDIT
# GET '/xxx/<id>/edit'
@bookings_blueprint.route("/bookings/<id>/edit", methods=["get"])
def edit_booking(id):
    booking = booking_repository.select(id)
    member = member_repository.select_all()
    gymclass = gymclass_repository.select_all()
    return render_template("bookings/edit.html", booking=booking, member=member, gymclass=gymclass)

# UPDATE
# PUT '/xxx/<id>'
@bookings_blueprint.route("/bookings/<id>", methods=["post"])
def update_booking(id):
    member_id = request.form["member_id"]
    gymclass_id = request.form["gymclass_id"]
    member = member_repository.select(member_id)
    gymclass = gymclass_repository.select(gymclass_id)
    booking = Booking(member, gymclass, id)
    booking_repository.update(booking)
    return redirect("/bookings")

# DELETE
# DELETE '/xxx/<id>'
@bookings_blueprint.route("/bookings/<id>/delete", methods=["post"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

