"""
Module used to realize interaction with database. Defines:
1. DepartmentService class -  implements business logic to unteract with department model.
"""
from department_app import db
from department_app.models.department import Department


class DepartmentService:
    """
    Department service class to perform detabase queries.
    """
    @staticmethod
    def get_all_dep():
        """
        Returns a list of all departments in db.
        Returns:
            all departments in db.
        """
        return Department.query.order_by(Department.id).all()

    @staticmethod
    def get_dep_by_name(department_name):
        """
        Returns a department specified by name.
        Returns:
            department specified by name.
        """
        return Department.query.filter_by(name=department_name).first()

    @staticmethod
    def get_dep_by_id(department_id):
        """
        Returns a department specified by id.
        Returns:
            department specified by id.
        """
        return Department.query.filter_by(id=department_id).first()

    @staticmethod
    def add_dep(name):
        """
        Adds new department to db.
        Args:
            name: department name.
        """
        try:
            department = Department(name)
            db.session.add(department)
            db.session.commit()
        except Exception as e:
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
    def delete(department_id):
        """
        Deletes department from db.
        Args:
            department_id (int): department id.
        Returns:
            bool: True or False
        """
        try:
            Department.query.filter_by(id=department_id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False
        return True

    @staticmethod
    def get_avg_salary(department):
        """
        Returns department average salary.
        Args:
            provided department
        Returns:
            department average salary value
        """
        employees_number = len(department.employees)
        avg_salary = 0
        try:
            for emp in department.employees:
                avg_salary += emp.salary
            avg_salary /= employees_number
            return round(avg_salary, 2)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def get_emp_count(department):
        """
        Calculates amount of employees within a department.
        Args:
            provided department
        Returns:
            employees within a department value.
        """
        return len(department.employees)
