from flask import Flask, jsonify
from flask_restful import Resource, Api

from sensor import Sensor

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class SensorData(Resource):
    def get(self):
        sensor = Sensor()
        data = sensor.get_data()
        return jsonify(data)


api.add_resource(HelloWorld, "/")
api.add_resource(SensorData, "/sensor")

if __name__ == "__main__":
    app.run(debug=True)
