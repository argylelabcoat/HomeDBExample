import falcon

from backend.models.score import ScoreRecord
from backend.storage.scores import ScoresStorage

storage = ScoresStorage()

class ScoresResource():
    def on_get(self, req, resp):
        allrecords = storage.getAll()
        
        scores = [record.as_dict for record in allrecords]

        resp.status = falcon.HTTP_200
        resp.media = {
            "scores": scores
        }

    def on_post(self, req, resp):
        try:
            record = ScoreRecord(req.media)
            record = storage.create(record)
        except IntegrityError:
            raise falcon.HTTPBadRequest(
                'Could not create score record'
            )
        resp.status = falcon.HTTP_201
        resp.media = {
            '_id': record.Id
        }