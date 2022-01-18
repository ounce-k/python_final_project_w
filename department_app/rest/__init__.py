"""
Module defines REST API implementation.
"""
from department_app import api
from department_app.rest.position import Position, PositionList
from department_app.rest.department import Department, DepartmentList
from department_app.rest.employee import Employee, EmployeeList, EmployeeSearchList


def initialize_api():
    """
    Attaches api routes to the Flask app.
    """
    api.add_resource(Department, '/api/departments/<department_id>')
    api.add_resource(DepartmentList, '/api/departments/')
    api.add_resource(Position, '/api/positions/<position_id>')
    api.add_resource(PositionList, '/api/positions/')
    api.add_resource(Employee, '/api/employees/<employee_id>')
    api.add_resource(EmployeeList, '/api/employees/')
    api.add_resource(EmployeeSearchList, '/api/employees/search')