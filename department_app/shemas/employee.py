from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from department_app import ma

from department_app.models.employee import Employee
from department_app.service.employee import EmployeeService

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta():
        model = Employee
        load_instanse = True
        include_fk = True