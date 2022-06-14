from flask import Flask, render_template, redirect, request
from flask import Blueprint
import pdb

from models.booking import Booking
from models.gymclass import Gymclass
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
    return render_template("bookings/index.html", bookings=all_bookings, title="Bookings")

# NEW
# GET '/xxx/new'
@bookings_blueprint.route("/bookings/new", methods = ["get"])
def new_booking():
    members = member_repository.select_all()
    gymclasses = gymclass_repository.select_all()
    return render_template("bookings/new.html", members=members, gymclasses=gymclasses, title="Add Booking")

# CREATE
# POST '/xxx'
@bookings_blueprint.route("/bookings", methods = ["post"])
def create_booking():
    member_id = request.form["member_id"]
    gymclass_id = request.form["gymclass_id"]
    member = member_repository.select(member_id)
    gymclass = gymclass_repository.select(gymclass_id)
    booking = Booking(member, gymclass)

    no_free_spaces = booking_repository.check_capacity(booking)
    if no_free_spaces == True:
        return render_template("bookings/full.html")

    if member.membership != "Plus" and int(gymclass.start_time.strftime("%H")) >= 16:
        return render_template("bookings/upgrade.html")

    else:
        booking_repository.save(booking)
        gymclass_repository.update(gymclass)
    return redirect("/bookings")


# DELETE
# DELETE '/xxx/<id>'
@bookings_blueprint.route("/bookings/<id>/delete", methods=["post"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

