from flask import Flask, abort, request, jsonify
from Database import Database

db = Database()

app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    if db.ready is not True:
        abort(503, "Database not connected.")


@app.route("/api/v1/new", methods=["POST"])
def new_timetable():
    return jsonify(request.json)


app.run(port=321)
