from flask import Flask, render_template

import repositories.gymclass_repository as gymclass_repository

from controllers.bookings_controller import bookings_blueprint
from controllers.gymclasses_controller import gymclasses_blueprint
from controllers.members_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(gymclasses_blueprint)
app.register_blueprint(members_blueprint)

@app.route("/")
def home():
    return render_template("index.html",)

if __name__ == "__main__":
    app.run(debug=True)




