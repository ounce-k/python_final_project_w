"""
Populates created database with the information.
"""

from datetime import date
from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.models.position import Position

class Populate:
    
    @staticmethod
    def populate():

        db.drop_all()
        db.create_all()
        dep_1 = Department('First department')
        dep_2 = Department('Second department')
        dep_3 = Department('Third department')
        
        pos_1 = Position('Director')
        pos_2 = Position('Operations Manager')
        pos_3 = Position('Office Manager')
        
        emp_1 = Employee('Mia', 'Yang', date(2011, 5, 21), 1500, 'abc1@example.com',  dep_1, pos_1)
        emp_2 = Employee('Marty', 'Wood', date(2013, 10, 15), 2500, 'abc2@example.com', dep_2, pos_2)
        emp_3 = Employee('Ashley', 'Miller', date(2018, 11, 23), 1000, 'abc3@example.com', dep_3, pos_3)
        emp_4 = Employee('Nick', 'Gupal', date(2020, 9, 5), 3500, 'abc4@example.com', dep_1, pos_2)
        
        db.session.add_all([dep_1, dep_2, dep_3])
        db.session.commit()
        db.session.add_all([pos_1, pos_2, pos_3])
        db.session.commit()
        db.session.add_all([emp_1, emp_2, emp_3, emp_4])
        db.session.commit()
        db.session.close()