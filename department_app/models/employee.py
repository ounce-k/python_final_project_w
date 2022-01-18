"""
Module defines Employee class, employee model that represents employee
"""

from sqlalchemy.orm import backref
from department_app import db


class Employee(db.Model):
    """
    Employee class object represents employee table in database.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey(
        'department.id', onupdate="CASCADE", ondelete="CASCADE"))
    position_id = db.Column(db.Integer, db.ForeignKey(
        'position.id', onupdate="CASCADE", ondelete="CASCADE"))

    def __init__(self, first_name, last_name, hire_date, salary, email, department=None, position=None):

        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.salary = salary
        self.email = email
        self.department = department
        self.position = position

    def __repr__(self):
        return f'Employee: {self.first_name} ' \
               f'{self.last_name}, ' \
               f'{self.hire_date}, ' \
               f'{self.salary}' \
               f'{self.email}' \
               f'{self.department}' \
               f'{self.position}'
