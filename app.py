from flask import Flask
from flask_restful import Resource, Api

from resources.images import Images
from resources.answer import Answer

app = Flask(__name__)

api = Api(app)

api.add_resource(Images, '/images')
api.add_resource(Answer, '/answer')


if __name__ == '__main__':
    app.run(debug=True)
