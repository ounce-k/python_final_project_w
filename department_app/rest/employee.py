from datetime import datetime
from os import stat
from flask import request
from flask.helpers import make_response
from sqlalchemy.util.langhelpers import decorator
from department_app.models import department
from flask_restful import Resource, abort

from department_app.shemas.employee import EmployeeSchema
from department_app.service.employee import EmployeeService
from department_app.service.department import DepartmentService
from department_app.service.position import PositionService
from department_app import logger

employee_service = EmployeeService()
department_service = DepartmentService()
position_service = PositionService()

employee_schema = EmployeeSchema()
employee_list_schema = EmployeeSchema(many=True)


class Employee(Resource):

    @staticmethod
    def get(employee_id):
        employee = employee_service.get_emp_by_id(employee_id)

        if not employee:
            logger.info(
                f'Failed to find employee with the id: {employee_id}')
            abort(404, description='No employee with provided id has been found')
        return employee_schema.dump(employee), 200

    @staticmethod
    def put(employee_id):
        employee = employee_service.get_emp_by_id(employee_id)

        if not employee:
            logger.info(
                f'Failed to find employee with the id: {employee_id}')
            abort(404, description='No employee with provided id has been found')

        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        email = request.json.get('email')
        hire_date = request.json.get('hire_date')
        salary = request.json.get('salary')

        department = department_service.get_dep_by_id(
            request.json.get('department_id'))
        position = position_service.get_pos_by_id(
            request.json.get('position_id'))

        if not department:
            logger.info(f'Department under provided id does not exist')
            abort(400, description='Department under provided id does not exist')

        if not position:
            logger.info(f'Position under provided id does not exist')
            abort(400, description='Position under provided id does not exist')

        if not (first_name and last_name and email and hire_date and salary and department and position):
            logger.info(f'Missing employee information')
            abort(400, description='Missing employee information')

        for emp in employee_service.get_all_emp():
            if email == emp.email:
                logger.info(f'Provided email name already exists')
                abort(406, description='Provided email name already exists')

        try:
            hire_date = datetime.strptime(hire_date, '%Y-%m-%d')
        except ValueError:
            logger.info(f'Incorrect hire date provided')
            abort(400, description='Incorrect hire date provided')

        try:
            salary = int(salary)
        except ValueError:
            logger.info(f'Incorrect salary type provided. Should be integer')
            abort(400, description='Incorrect salary type provided. Should be integer')

        employee.first_name = first_name
        employee.last_name = last_name
        employee.email = email
        employee.hire_date = hire_date
        employee.salary = salary
        employee.department = department
        employee.position = position

        employee_service.save_changes()
        logger.info('Employee was successfully changed')
        return employee_schema.dump(employee), 200

    @staticmethod
    def delete(employee_id):
        employee = employee_service.get_emp_by_id(employee_id)

        if not employee:
            logger.info(
                f'Failed to find employee with the id: {employee_id}')
            abort(404, description='No employee with provided id has been found')

        employee_service.delete(employee_id)
        logger.info(
            f'Employee under the id {employee_id} was successfully deleted')
        return make_response({'message': 'Employee has been successfully deleted'}, 200)


class EmployeeList(Resource):

    @staticmethod
    def get():
        employees = employee_service.get_all_emp()
        return employee_list_schema.dump(employees), 200

    @staticmethod
    def post():
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        email = request.json.get('email')
        hire_date = request.json.get('hire_date')
        salary = request.json.get('salary')
        department = request.json.get('department_id')
        position = request.json.get('position_id')

        dep = department_service.get_dep_by_id(
            request.json.get('department_id'))
        pos = position_service.get_pos_by_id(request.json.get('position_id'))

        if not dep:
            logger.info(f'Department under provided id does not exist')
            abort(400, description='Department under provided id does not exist')

        if not pos:
            logger.info(f'Position under provided id does not exist')
            abort(400, description='Position under provided id does not exist')

        if not (first_name and last_name and email and hire_date and salary and department and position):
            logger.info(f'Missing employee information')
            abort(400, description='Missing employee information')

        for emp in employee_service.get_all_emp():
            if email == emp.email:
                logger.info(f'Provided email name already exists')
                abort(406, description='Provided email name already exists')

        try:
            hire_date = datetime.strptime(hire_date, '%Y-%m-%d')
        except ValueError:
            logger.info(f'Incorrect hire date provided')
            abort(400, description='Incorrect hire date provided')

        try:
            salary = int(salary)
        except ValueError:
            logger.info(f'Incorrect salary type provided. Should be integer')
            abort(400, description='Incorrect salary type provided. Should be integer')

        employee_service.add_emp(
            first_name, last_name, hire_date, salary, email, dep.name, pos.name)
        logger.info(f'New employee under the email {email} was created')
        new_emp = employee_service.get_emp_by_email(email)
        return employee_schema.dump(new_emp), 200


class EmployeeSearchList(Resource):

    @staticmethod
    def get():
        date_to = request.json.get('date_to')
        date_from = request.json.get('date_from')

        try:
            date_to = datetime.strptime(date_to, '%Y-%m-%d')
            date_from = datetime.strptime(date_from, '%Y-%m-%d')
        except (ValueError, TypeError):
            logger.info(f'Incorrect dates provided')
            abort(400, description='Incorrect dates provided')

        employees = employee_service.get_emp_by_hire_date(date_from, date_to)
        return employee_list_schema.dump(employees, many=True), 200
