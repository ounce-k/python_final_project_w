


from department_app import db
from department_app.models.department import Department


class DepartmentService:

    @staticmethod
    def get_all_dep():
        return Department.query.order_by(Department.id).all()

    @staticmethod
    def get_dep_by_name(department_name):
        return Department.query.filter_by(name=department_name).first()

    @staticmethod
    def get_dep_by_id(department_id):
        return Department.query.filter_by(id=department_id).first()

    @staticmethod
    def add_dep(name):
        try:
            department = Department(name)
            db.session.add(department)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def save_changes():  # for edit
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def delete(department_id):
        try:
            Department.query.filter_by(id=department_id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False
        return True

    @staticmethod
    def get_avg_salary(department):
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
        return len(department.employees)