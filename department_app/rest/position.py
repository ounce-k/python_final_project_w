"""
Positions REST API, module defines:
1. Position class that is position API class
2. PositionList class that is positions list API class
"""
from flask import request
from flask.helpers import make_response
from flask_restful import Resource, abort

from department_app.shemas.position import PositionSchema
from department_app.service.position import PositionService
from department_app import logger

position_service = PositionService()
position_schema = PositionSchema()
position_list_schema = PositionSchema(many=True)


class Position(Resource):
    """
    REST API for Position model.
    Can be accessed by url /api/positions/<position_id>.
    Includes GET, PUT, DELETE methods.
    """
    @staticmethod
    def get(position_id):
        """
        GET method for position.
        Args:
            position_id (int): position id
        Returns:
            json representation of position and status code or error message and status code
        """
        try:
            position = position_service.get_pos_by_id(position_id)
            return position_schema.dump(position), 200
        except AttributeError as e:
            logger.info(
                f'Failed to find position with the id: {position_id}')
            abort(404, description='No position with provided id has been found')

    @staticmethod
    def put(position_id):
        """
        PUT method for position.
        Args:
            position_id (int): position id
        Returns:
            json representation of updated position and status code or error message and status code
        """
        position = position_service.get_pos_by_id(position_id)
        if not position:
            logger.info(
                f'Failed to find position with the id: {position_id}')
            abort(404, description='No position with provided id has been found')

        name = request.json.get('name')
        if not name:
            logger.info(f'No position name provided')
            abort(400, description='No position name provided')

        for pos in position_service.get_all_pos():
            if name == pos.name:
                logger.info(f'Provided position name already exists')
                abort(406, description='Provided position name already exists')

        position.name = name
        position_service.save_changes()
        logger.info('Position name was successfully changed')
        return position_schema.dump(position), 200

    @staticmethod
    def delete(position_id):
        """
        DELETE method for position.
        Args:
            position_id (int): position id
        Returns:
            message and status code
        """
        position = position_service.get_pos_by_id(position_id)

        if not position:
            logger.info(
                f'Failed to find position with the id: {position_id}')
            abort(404, description='No position with provided id has been found')

        name = position.name
        position_service.delete(position_id)

        logger.info(
            f'Position under the name "{name}" was successfully deleted')
        return make_response({'message': 'Position has been successfully deleted'}, 200)


class PositionList(Resource):
    """
    REST API for PositionList model.
    Can be accessed by url '/api/positions/'.
    Includes GET, POST methods.
    """
    @staticmethod
    def get():
        """
        GET method for positions list.
        Returns:
            json representation of positions list and status code or error message and status code
        """
        positions = position_service.get_all_pos()
        return position_list_schema.dump(positions), 200

    @staticmethod
    def post():
        """
        POST method for positions list.
        Returns:
            json representation of created position and status code or error message and status code
        """
        name = request.json.get('name')

        if not name:
            logger.info(f'Incorrect position name provided')
            abort(400, description='Incorrect position name provided')

        for pos in position_service.get_all_pos():
            if name == pos.name:
                logger.info(f'Provided position name already exists')
                abort(406, description='Provided position name already exists')

        position_service.add_pos(name)
        logger.info(f'New position under the name {name} was created')
        new_dep = position_service.get_pos_by_name(name)
        return position_schema.dump(new_dep), 200
