import os
import secrets

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
server = os.environ.get('MYSQL_SERVER')
databese = os.environ.get('MYSQL_DATABASE')

class Configuration:
    """
    Class for app configuration.
    """
    DEBUG = True
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{server}/{databese}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfiguration:
    """
    Class for app testing configuration.
    """
    TESTING = True
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tests', 'test_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False