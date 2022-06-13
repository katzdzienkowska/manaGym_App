from flask import Flask, render_template
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

# CREATE
# POST '/xxx'

# SHOW
# GET '/xxx/<id>'

# EDIT
# GET '/xxx/<id>/edit'

# UPDATEß
# PUT '/xxx/<id>'

# DELETE
# DELETE '/xxx/<id>'