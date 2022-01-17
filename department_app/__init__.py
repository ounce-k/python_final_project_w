"""[summary]"""

import logging
import sys

from flask import Flask
from flask_restful import Api
from department_app.configuration import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('logFile.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

app = Flask(__name__)
app.config.from_object(Configuration)

api = Api(app)
db = SQLAlchemy(app)

from department_app.models import department
from department_app.models import employee
from department_app.models import position


if not database_exists(Configuration.SQLALCHEMY_DATABASE_URI):
    create_database(Configuration.SQLALCHEMY_DATABASE_URI)
    db.create_all()
    
db.drop_all()

from department_app.populate import Populate
db.create_all()
# Populate.populate() #use or not?

ma = Marshmallow(app)
migrate = Migrate(app, db)


from department_app.rest import initialize_api
initialize_api()

from department_app import views
app.register_blueprint(views.m_bp)