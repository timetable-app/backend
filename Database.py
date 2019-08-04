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
