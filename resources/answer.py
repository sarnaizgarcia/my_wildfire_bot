import flask

from flask_restful import Resource

from helper.response_factory import response_factory
from controllers.answer_controller import answer_controller


class Answer(Resource):

    @classmethod
    def post(cls):
        answer = flask.request.json
        return response_factory(answer_controller(answer))
