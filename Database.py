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

from pymongo import MongoClient
import os


class Database:
    def __init__(self):
        self.ready = False
        self.dbSetup()

    def dbSetup(self):
        self.client = MongoClient(os.getenv("MONGO_URI", "mongodb://hi:*hi123@ds259377.mlab.com:59377/timetable"))
        self.db = self.client["timetable"]
        self.ready = True

    def new(self, date: str, time: str, subject: str, topic: str):
        if self.ready is not True:
            return
        else:
            self.db["timetable"].find_one_and_update(
                {"date": date},
                {"$set": {time: time, subject: subject, topic: topic}},
                upsert=True,
            )
            return True
