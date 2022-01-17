
from os import stat
from flask import request
from flask.helpers import make_response
from flask_restful import Resource, abort

from department_app.shemas.department import DepartmentSchema
from department_app.service.department import DepartmentService
from department_app import logger

department_service = DepartmentService()
department_schema = DepartmentSchema()
department_list_schema = DepartmentSchema(many=True)



class Department(Resource):

    @staticmethod
    def get(department_id):
        try:
            department = department_service.get_dep_by_id(department_id)
            return department_schema.dump(department), 200
        except AttributeError as e:
            logger.info(
                f'Failed to find department with the id: {department_id}')
            abort(404, description='No department with provided id has been found')

    @staticmethod
    def put(department_id):
        department = department_service.get_dep_by_id(department_id)
        if not department:
            logger.info(
                f'Failed to find department with the id: {department_id}')
            abort(404, description='No department with provided id has been found')

        name = request.json.get('name')
        if not name:
            logger.info(f'No department name provided')
            abort(400, description='No department name provided')

        for dep in department_service.get_all_dep():
            if name == dep.name:
                logger.info(f'Provided department name already exists')
                abort(406, description='Provided department name already exists')

        department.name = name
        department_service.save_changes()
        logger.info('Department name was successfully changed')
        return department_schema.dump(department), 200

    @staticmethod
    def delete(department_id):
        department = department_service.get_dep_by_id(department_id)
        
        if not department:
            logger.info(
                f'Failed to find department with the id: {department_id}')
            abort(404, description='No department with provided id has been found')
  
        name = department.name
        department_service.delete(department_id)

        logger.info(
            f'Department under the name "{name}" was successfully deleted')
        return make_response({'message': 'Department has been successfully deleted'}, 200)

class DepartmentList(Resource):

    @staticmethod
    def get():
        departments = department_service.get_all_dep()
        return department_list_schema.dump(departments), 200

    @staticmethod
    def post():
        name = request.json.get('name')

        if not name:
            logger.info(f'Incorrect department name provided')
            abort(400, description='Incorrect department name provided')

        for dep in department_service.get_all_dep():
            if name == dep.name:
                logger.info(f'Provided department name already exists')
                abort(406, description='Provided department name already exists')

        department_service.add_dep(name)
        logger.info(f'New department under the name {name} was created')
        new_dep = department_service.get_dep_by_name(name)
        return department_schema.dump(new_dep), 200