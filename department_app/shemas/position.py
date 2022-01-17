

from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from department_app import ma

from department_app.models.position import Position
from department_app.service.position import PositionService

class PositionSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta():
        model = Position
        load_instanse = True
        include_fk = True
    
    
    avg_salary = fields.Method('average_salary')
    number_of_employees = fields.Method('count_employees')
    
    @classmethod
    def average_salary(cls, position):
        return PositionService.get_avg_salary(position)
    
    @classmethod
    def count_employees(cls, position):
        return PositionService.get_emp_count(position)