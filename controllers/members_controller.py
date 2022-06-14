from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/xxx'
@members_blueprint.route("/members")
def members():
    all_members = member_repository.select_all()
    return render_template("members/index.html", members=all_members)

# NEW
# GET '/xxx/new'
@members_blueprint.route("/members/new", methods = ["get"])
def new_member():
    return render_template("members/new.html") #add title later

# CREATE
# POST '/xxx'
@members_blueprint.route("/members", methods = ["post"])
def create_member():
    name = request.form["name"]
    dob = request.form["dob"]
    membership = request.form["membership"]
    active = request.form["active"]
    member = Member(name, dob, membership, active)
    member_repository.save(member)
    return redirect("/members")

# SHOW
# GET '/xxx/<id>'
@members_blueprint.route("/members/<id>")
def show_member(id):
    booked_gymclasses = member_repository.list_of_gymclasses_booked(id)
    found_member = member_repository.select(id)
    return render_template("members/show.html", member=found_member, booked_gymclasses=booked_gymclasses)

# EDIT
# GET '/xxx/<id>/edit'
@members_blueprint.route("/members/<id>/edit", methods=["get"])
def edit_member(id):
    edit_member = member_repository.select(id)
    return render_template("members/edit.html", member=edit_member)

# UPDATE
# PUT '/xxx/<id>'
@members_blueprint.route("/members/<id>", methods=["post"])
def update_member(id):
    name = request.form["name"]
    dob = request.form["dob"]
    membership = request.form["membership"]
    active = request.form["active"]
    member = Member(name, dob, membership, active, id)
    member_repository.update(member)
    return redirect("/members")

# DELETE
# DELETE '/xxx/<id>'
@members_blueprint.route("/members/<id>/delete", methods=["post"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")

