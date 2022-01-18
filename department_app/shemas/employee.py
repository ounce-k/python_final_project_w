"""
Employee schema module is used to perform serialization and deserialization
on employees. Defines:
1. EmployeeSchema class - employees serialization and deserialization schema
"""
from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from department_app import ma

from department_app.models.employee import Employee
from department_app.service.employee import EmployeeService

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    """
    Employee serialization and deserialization schema.
    """
    # pylint: disable=too-few-public-methods
    class Meta():
        """
        Metadata for schema.
        """
        model = Employee # model for generating schema
        load_instanse = True # deserialize to model schema
        include_fk = True # include foreign key to schema