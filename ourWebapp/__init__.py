"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER = './files/'  # make sure the folder ./file/ is created before running
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import ourWebapp.views
