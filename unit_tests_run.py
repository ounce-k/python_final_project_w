"""
Module initializes tests.
"""
import unittest

from flask import Flask

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from department_app.populate import Populate
from department_app.configuration import TestingConfiguration


from department_app.tests.department_service import TestDepartmentService
from department_app.tests.position_sevice import TestPositionService
from department_app.tests.employee_service import TestEmployeeService
from department_app.tests.department_view import TestDepartmentView
from department_app.tests.position_view import TestPositionView
from department_app.tests.employees_view import TestEmployeeView

# from sqlalchemy_utils import database_exists, create_database

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDepartmentService('testDepartments'))
    suite.addTest(TestPositionService('testPositions'))
    suite.addTest(TestEmployeeService('testEmployees'))
    suite.addTest(unittest.makeSuite(TestDepartmentView))
    suite.addTest(unittest.makeSuite(TestPositionView))
    suite.addTest(unittest.makeSuite(TestEmployeeView))
    return suite

if __name__ == '__main__':
    app = Flask(__name__)

    app.config.from_object(TestingConfiguration)

    api = Api(app)
    db = SQLAlchemy(app)

    app_context = app.app_context()
    app_context.push()
    
    Populate.populate()
    
    runner = unittest.TextTestRunner()
    runner.run(suite())
    
    db.session.remove()
    db.drop_all()