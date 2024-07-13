from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
import requests

from sensor import Sensor
from config import setup_logging

app = Flask(__name__)
api = Api(app)

# Setup logging
logger = setup_logging()


class SensorData(Resource):
    def get(self):
        """Handle GET request to retrieve sensor data and send it to another API."""
        sensor = Sensor()
        data = sensor.get_data()
        logger.info(f"Received sensor data: {data}")
        response = self.send_post_request(data)
        return response

    def send_post_request(self, data):
        """Send POST request with sensor data to another API."""
        url = "http://127.0.0.1:5000/sensor-data"  # Replace with API endpoint
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return make_response(
                jsonify({"message": "Data sent successfully"}), response.status_code
            )
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            return make_response(
                jsonify({"message": f"HTTP error occurred: {http_err}"}),
                response.status_code,
            )
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Error sending POST request: {req_err}")
            return make_response(
                jsonify({"message": f"Error sending POST request: {req_err}"}), 500
            )

    # POST method only for testing purposes
    def post(self):
        """Handle POST request to receive and process sensor data."""
        if not request.is_json:
            return {"message": "Request must be JSON"}, 400

        data = request.get_json()
        print(f"Received data: {data}")
        return make_response(jsonify({"received": data}), 201)


api.add_resource(SensorData, "/sensor-data")

if __name__ == "__main__":
    app.run(debug=True)
