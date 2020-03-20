from flask import Flask
from flask_restful import Resource, Api

from image_resource import Image

app = Flask(__name__)

api = Api(app)

api.add_resource(Image, '/')

if __name__ == '__main__':
    app.run(debug=True)
