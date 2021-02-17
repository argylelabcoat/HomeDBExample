import json
import logging
import uuid
from wsgiref import simple_server

import falcon
import requests


from backend.controllers.scores import ScoresResource

# Configure your WSGI server to load "things.app" (app is a WSGI callable)
app = falcon.API()

scoresController = ScoresResource()
app.add_route('/scores', scoresController)


if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 5000, app)
    httpd.serve_forever()