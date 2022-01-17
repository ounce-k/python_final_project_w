
from department_app import db
from department_app.models.position import Position

class PositionService:

    @staticmethod
    def get_all_pos():
        return Position.query.order_by(Position.id).all()
    
    @staticmethod
    def get_pos_by_name(position_name):
        return Position.query.filter_by(name=position_name).first()
    
    @staticmethod
    def get_pos_by_id(position_id):
        return Position.query.filter_by(id=position_id).first()
    
    @staticmethod
    def save_changes(): #for edit
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    
    @staticmethod
    def add_pos(name):
        try:
            position = Position(name)
            db.session.add(position)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    
    @staticmethod
    def delete(position_id):
        try:
            Position.query.filter_by(id=position_id).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False
        return True
    
    @staticmethod 
    def get_avg_salary(position):
        employees_number = len(position.employees)
        avg_salary = 0
        try:
            for emp in position.employees:
                avg_salary += emp.salary
            avg_salary /= employees_number
            return round(avg_salary, 2)
        except ZeroDivisionError:
            return 0
                        
    @staticmethod 
    def get_emp_count(position):
        return len(position.employees)