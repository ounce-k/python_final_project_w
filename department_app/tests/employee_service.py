
import unittest
from datetime import date

from department_app.models.employee import Employee
from department_app.service.employee import EmployeeService
from department_app.service.position import PositionService
from department_app.service.department import DepartmentService

employee_service = EmployeeService()

class TestEmployeeService(unittest.TestCase):
    
    def test_get_all(self):
        self.assertEqual(4, len(employee_service.get_all_emp()))
    
    def test_get_emp_by_id(self):
        self.assertEqual(1, employee_service.get_emp_by_id(1).id)
    
    def test_get_by_first_name(self):
        self.assertEqual('Mia', employee_service.get_emp_by_firstname('Mia').first_name)
    
    def test_get_by_last_name(self):
        self.assertEqual('Yang', employee_service.get_emp_by_lastname('Yang').last_name)

    def test_get_by_email(self):
        self.assertEqual('abc1@example.com', employee_service.get_emp_by_email('abc1@example.com').email)
    
    def test_add_emp(self):
        employee_service.add_emp('Betty', 'Brown', date(2021, 9, 5), 2000, 'abc5@example.com', DepartmentService.get_dep_by_id(1).name, PositionService.get_pos_by_id(1).name)
        self.assertEqual(5, Employee.query.count())
    
    def test_delete_emp(self):
        employee_service.delete(4)
        self.assertEqual(4, len(employee_service.get_all_emp()))
    
    def test_save_changes(self):
        updated_emp = employee_service.get_emp_by_id(1)
        updated_emp.first_name = 'Harry'
        updated_emp.last_name = 'Smith'
        updated_emp.salary = 1234
        updated_emp.hire_date = date(2019, 8, 3)
        employee_service.save_changes()
        updated = employee_service.get_emp_by_id(1)
        self.assertEqual('Harry', updated.first_name)
        self.assertEqual('Smith', updated.last_name)
        self.assertEqual(1234, updated.salary)
        self.assertEqual(date(2019, 8, 3), updated.hire_date)
    
    def test_get_emp_by_hire_date(self):
        self.assertEqual(date(2011, 5, 21), employee_service.get_emp_by_id(1).hire_date)