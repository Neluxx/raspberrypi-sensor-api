from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
import requests

from sensor import Sensor
from dotenv import load_dotenv
import os

app = Flask(__name__)
api = Api(app)

load_dotenv()


class SensorData(Resource):
    def get(self):
        """Handle GET request to retrieve sensor data and send it to another API."""
        sensor = Sensor()
        data = sensor.get_data()
        response = self.send_post_request(data)
        return response

    def send_post_request(self, data):
        """Send POST request with sensor data to another API."""
        url = os.getenv("API_URL")
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return make_response(
                jsonify({"message": "Data sent successfully"}), response.status_code
            )
        except requests.exceptions.HTTPError as http_err:
            return make_response(
                jsonify({"message": f"HTTP error occurred: {http_err}"}),
                response.status_code,
            )
        except requests.exceptions.RequestException as req_err:
            return make_response(
                jsonify({"message": f"Error sending POST request: {req_err}"}), 500
            )


api.add_resource(SensorData, "/sensor-data")

if __name__ == "__main__":
    app.run(debug=True)
