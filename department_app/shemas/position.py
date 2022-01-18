"""
Position schema module is used to perform serialization and deserialization
on positions. Defines:
1. PositionSchema class - position serialization and deserialization schema
"""
from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from department_app import ma

from department_app.models.position import Position
from department_app.service.position import PositionService

class PositionSchema(ma.SQLAlchemyAutoSchema):
    """
    Position serialization and deserialization schema.
    """
    # pylint: disable=too-few-public-methods
    class Meta():
        """
        Metadata for schema.
        """
        model = Position # model for generating schema
        load_instanse = True # deserialize to model schema
        include_fk = True # include foreign key to schema
    
    avg_salary = fields.Method('average_salary')
    number_of_employees = fields.Method('count_employees')
    
    @classmethod
    def average_salary(cls, position):
        """
        Returns position average salary.
        Args:
            provided position
        Returns:
            position average salary value
        """
        return PositionService.get_avg_salary(position)
    
    @classmethod
    def count_employees(cls, position):
        """
        Calculates amount of employees within a position.
        Args:
            provided position
        Returns:
            employees within a position value.
        """
        return PositionService.get_emp_count(position)