"""[summary]"""

from sqlalchemy.orm import backref
from department_app import db


class Department(db.Model):
    """å

    """
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    employees = db.relationship(
        'Employee', cascade='all, delete', backref='department', lazy=True)

    def __init__(self, name, employees=[]):
        self.name = name
        self.employees = employees

    def __repr__(self):
        return f'{self.name}'
