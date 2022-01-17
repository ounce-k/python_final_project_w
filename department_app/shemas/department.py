
from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import post_load
from department_app import ma

from department_app.models.department import Department
from department_app.service.department import DepartmentService
from department_app.shemas.employee import EmployeeSchema

class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta():
        model = Department
        load_instanse = True
        include_fk = True
    
    # employees = ma.Nested(EmployeeSchema, many=True)
    avg_salary = fields.Method('average_salary')
    number_of_employees = fields.Method('count_employees')
    
    @classmethod
    def average_salary(cls, department):
        return DepartmentService.get_avg_salary(department)
    
    @classmethod
    def count_employees(cls, department):
        return DepartmentService.get_emp_count(department)
    
    
    
    
    # @post_load
    # def make_department(self, data, **kwargs):
    #     return Department(**data)