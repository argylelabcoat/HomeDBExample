import configparser
import pycouchdb

from backend.models.score import ScoreRecord

class ScoresStorage():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('/var/lib/app/couch.ini')
        password = config.get('admins','admin')

        self.dbserver = pycouchdb.Server(f'http://admin:{password}@db:5984/')
        try:
            self.scoresdb = self.dbserver.database("scores")
        except pycouchdb.exceptions.NotFound:
            self.scoresdb = self.dbserver.create("scores")

    def getAll(self):
        allrecords = self.scoresdb.all(wrapper=ScoreRecord)
        return allrecords

    def create(self, record):
        return self.scoresdb.save(record.as_dict())

