"""
Module used to realize interaction with database. Defines:
1. EmployeeService class -  implements business logic to unteract with position model.
"""
from department_app import db
from department_app.models.employee import Employee
from department_app.service.department import DepartmentService
from department_app.service.position import PositionService


class EmployeeService:
    """
    Employee service class to perform detabase queries.
    """
    @staticmethod
    def get_all_emp():
        """
        Returns a list of all employees in db.
        Returns:
            all employees in db.
        """
        return Employee.query.order_by(Employee.id).all()

    @staticmethod
    def get_emp_by_id(employee_id):
        """
        Returns an employee specified by id.
        Returns:
            employee specified by id.
        """
        return Employee.query.filter_by(id=employee_id).first()

    @staticmethod
    def get_emp_by_firstname(employee_first_name):
        """
        Returns an employee specified by first name.
        Returns:
            employee specified by first name.
        """
        return Employee.query.filter_by(first_name=employee_first_name).first()

    @staticmethod
    def get_emp_by_lastname(employee_last_name):
        """
        Returns an employee specified by last name.
        Returns:
            employee specified by last name.
        """
        return Employee.query.filter_by(last_name=employee_last_name).first()

    @staticmethod
    def get_emp_by_email(employee_email):
        """
        Returns an employee specified by email.
        Returns:
            employee specified by email.
        """
        return Employee.query.filter_by(email=employee_email).first()

    @staticmethod
    def get_emp_by_hire_date(employee_date_from, employee_date_to):
        """
        Returns an employee specified by hire date.
        Returns:
            employee specified by hire date.
        """
        return Employee.query.filter(Employee.hire_date.between(employee_date_from, employee_date_to)).all()

    @staticmethod
    def get_emp_for_dep(department_id):
        """
        Returns a list of all employees in specified department.
        Returns:
            all employees in specified department.
        """
        return Employee.query.filter_by(department_id=department_id).all()

    @staticmethod
    def add_emp(first_name, last_name, hire_date, salary, email, department, position):
        """
        Adds employee to db.
        Args:
            first_name (str): employee first name
            last_name (str): employee last name
            hire_date (str): employee hire date
            salary (int): employee salary
            email (str): employee email
            department (str): employee department name
            position (str): employee position name
        """
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
        """
        Saves changes in db.
        """
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def delete(employee_id):
        """
        Deletes employee from db.
        Args:
            employee_id (int): employee id.
        Returns:
            bool: True or False
        """
        try:
            Employee.query.filter_by(id=employee_id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False
        return True
