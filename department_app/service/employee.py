"""[summary]"""

from department_app import db
from department_app.models.employee import Employee
from department_app.service.department import DepartmentService
from department_app.service.position import PositionService


class EmployeeService:

    @staticmethod
    def get_all_emp():
        return Employee.query.order_by(Employee.id).all()

    @staticmethod
    def get_emp_by_id(employee_id):
        return Employee.query.filter_by(id=employee_id).first()

    @staticmethod
    def get_emp_by_firstname(employee_first_name):
        return Employee.query.filter_by(first_name=employee_first_name).first()

    @staticmethod
    def get_emp_by_lastname(employee_last_name):
        return Employee.query.filter_by(last_name=employee_last_name).first()

    @staticmethod
    def get_emp_by_email(employee_email):
        return Employee.query.filter_by(email=employee_email).first()

    @staticmethod
    def get_emp_by_hire_date(employee_date_from, employee_date_to):
        return Employee.query.filter(Employee.hire_date.between(employee_date_from, employee_date_to)).all()

    @staticmethod
    def get_emp_for_dep(department_id):
        return Employee.query.filter_by(department_id=department_id).all()

    @staticmethod
    def add_emp(first_name, last_name, hire_date, salary, email, department, position):
        try:
            employee = Employee(first_name, last_name, hire_date, salary, email, DepartmentService.get_dep_by_name(
                department), PositionService.get_pos_by_name(position))
            db.session.add(employee)
            db.session.commit()
            # print("IN A TRY")
        except Exception as e:
            print(e)
            db.session.rollback()

    @staticmethod
    def save_changes():  # for edit
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def delete(employee_id):
        try:
            Employee.query.filter_by(id=employee_id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False
        return True
