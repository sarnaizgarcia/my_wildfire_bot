import flask

from flask_restful import Resource

from helper.response_factory import response_factory
from controllers.image_controller import image_controller
from controllers.location_controller import location_ctrl


class Images(Resource):

    @classmethod
    def post(cls):
        params = flask.request.json
        return response_factory(location_ctrl(params))

    @classmethod
    def get(cls):
        return response_factory(image_controller())
