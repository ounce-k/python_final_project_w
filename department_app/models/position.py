"""[summary]"""

from sqlalchemy.orm import backref
from department_app import db


class Position(db.Model):
    """

    """
    __tablename__ = 'position'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    employees = db.relationship(
        'Employee', cascade='all, delete', backref='position', lazy=True)

    def __init__(self, name, employees=[]):
        self.name = name
        self.employees = employees

    def __repr__(self):
        return f'{self.name}'