"""
Module used to realize interaction with database. Defines:
1. PositionService class -  implements business logic to unteract with position model.
"""
from department_app import db
from department_app.models.position import Position


class PositionService:
    """
    Position service class to perform detabase queries.
    """
    @staticmethod
    def get_all_pos():
        """
        Returns a list of all positions in db.
        Returns:
            all positions in db.
        """
        return Position.query.order_by(Position.id).all()

    @staticmethod
    def get_pos_by_name(position_name):
        """
        Returns a position specified by name.
        Returns:
            position specified by name.
        """
        return Position.query.filter_by(name=position_name).first()

    @staticmethod
    def get_pos_by_id(position_id):
        """
        Returns a position specified by id.
        Returns:
            position specified by id.
        """
        return Position.query.filter_by(id=position_id).first()

    @staticmethod
    def save_changes():  # for edit
        """
        Saves changes in db.
        """
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def add_pos(name):
        """
        Adds new position to db.
        Args:
            name: position name.
        """
        try:
            position = Position(name)
            db.session.add(position)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def delete(position_id):
        """
        Deletes position from db.
        Args:
            position_id (int): position id.
        Returns:
            bool: True or False
        """
        try:
            Position.query.filter_by(id=position_id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False
        return True

    @staticmethod
    def get_avg_salary(position):
        """
        Returns position average salary.
        Args:
            provided position
        Returns:
            position average salary value
        """
        employees_number = len(position.employees)
        avg_salary = 0
        try:
            for emp in position.employees:
                avg_salary += emp.salary
            avg_salary /= employees_number
            return round(avg_salary, 2)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def get_emp_count(position):
        """
        Calculates amount of employees within a position.
        Args:
            provided position
        Returns:
            employees within a position value.
        """
        return len(position.employees)
