"""
 Copyright (C) 2019 timetable-app
 
 This file is part of backend.
 
 backend is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 backend is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with backend.  If not, see <http://www.gnu.org/licenses/>.
"""

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
