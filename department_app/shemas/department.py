"""
Department schema module is used to perform serialization and deserialization
on departments. Defines:
1. DepartmentSchema class - department serialization and deserialization schema
"""
from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from department_app import ma

from department_app.models.department import Department
from department_app.service.department import DepartmentService
from department_app.shemas.employee import EmployeeSchema

class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    """
    Department serialization and deserialization schema.
    """
    # pylint: disable=too-few-public-methods
    class Meta():
        """
        Metadata for schema.
        """
        model = Department # model for generating schema
        load_instanse = True # deserialize to model schema
        include_fk = True # include foreign key to schema
    
    avg_salary = fields.Method('average_salary')
    number_of_employees = fields.Method('count_employees')
    
    @classmethod
    def average_salary(cls, department):
        """
        Returns department average salary.
        Args:
            provided department
        Returns:
            department average salary value
        """
        return DepartmentService.get_avg_salary(department)
    
    @classmethod
    def count_employees(cls, department):
        """
        Calculates amount of employees within a department.
        Args:
            provided department
        Returns:
            employees within a department value.
        """
        return DepartmentService.get_emp_count(department)
