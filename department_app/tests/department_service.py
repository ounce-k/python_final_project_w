import unittest
from department_app.service.department import DepartmentService

department_service = DepartmentService()

class TestDepartmentService(unittest.TestCase):
    
    def test_get_all(self):
        self.assertEqual(3, len(department_service.get_all_dep()))
    
    def test_get_dep_by_id(self):
        self.assertEqual(1, department_service.get_dep_by_id(1).id)
    
    def test_get_by_name(self):
        self.assertEqual('First department', department_service.get_dep_by_name('First department').name)
    
    def test_delete(self):
        department_service.delete(4)
        self.assertEqual(3, len(department_service.get_all_dep()))
        
    def test_add_dep(self):
        department_service.add_dep('Super test name')
        self.assertEqual(4, len(department_service.get_all_dep()))
        
    def test_save_changes(self):
        updated_dep = department_service.get_dep_by_id(1)
        updated_dep.name = 'New updated name'
        department_service.save_changes()
        self.assertEqual('New updated name', updated_dep.name)
    
    def test_average_salary(self):
        dep = department_service.get_dep_by_id(1)
        self.assertEqual(2500, department_service.get_avg_salary(dep))
    
    def test_count_emp(self):
        dep = department_service.get_dep_by_id(1)
        self.assertEqual(2, department_service.get_emp_count(dep))
    
    