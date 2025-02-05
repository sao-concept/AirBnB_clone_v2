#!/usr/bin/python3
from flask import Flask
from models import storage
from flask import render_template

"""
This script starts a Flask web application:
"""
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_list_route():
    """
    This function list all cities a of states: display a HTML page: (inside the tag BODY)
    Returns:
        html: template that lists states, cities & amenity sort by name A->Z
    """
    data = {
        "states": storage.all("State").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("10-hbnb_filters.html", models=data)


@app.teardown_appcontext
def close_db(exception=None):
    """
    This function remove the current SQLAlchemy Session after each
    request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
