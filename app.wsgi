import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, "/var/www/raspberrypi-sensor-api")

# Set the environment variable for the Flask application
os.environ['FLASK_APP'] = 'app.py'

# If you are using a virtual environment, activate it
activate_this = '/var/www/raspberrypi-sensor-api/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import your Flask application
from app import app as application
