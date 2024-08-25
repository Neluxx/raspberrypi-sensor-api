import sys
import os
import site
 
# Add the project directory to the Python path
sys.path.insert(0, "/var/www/raspberrypi-sensor-api")
 
# Set the environment variable for the Flask application
os.environ['FLASK_APP'] = 'app.py'
 
# If you are using a virtual environment, activate it
venv_path = '/var/www/raspberrypi-sensor-api/venv'
site.addsitedir(os.path.join(venv_path, 'lib', 'python3.9', 'site-packages'))
 
# Import your Flask application
from app import app as application
