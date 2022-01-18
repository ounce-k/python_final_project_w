import unittest
from department_app.service.position import PositionService

position_service = PositionService()

class TestPositionService(unittest.TestCase):
    
    def testPositions(self):
        self.test_get_all()
        self.test_get_pos_by_id()
        self.test_get_by_name()
        self.test_add_pos()
        self.test_save_changes()
        self.test_average_salary()
        self.test_count_emp()
        self.test_delete()
    
    def test_get_all(self):
        self.assertEqual(3, len(position_service.get_all_pos()))
    
    def test_get_pos_by_id(self):
        self.assertEqual(1, position_service.get_pos_by_id(1).id)
    
    def test_get_by_name(self):
        self.assertEqual('Director', position_service.get_pos_by_name('Director').name)

    def test_add_pos(self):
        position_service.add_pos('Super test name')
        self.assertEqual(4, len(position_service.get_all_pos()))
        
    def test_save_changes(self):
        updated_pos = position_service.get_pos_by_id(4)
        updated_pos.name = 'New updated name'
        position_service.save_changes()
        self.assertEqual('New updated name', updated_pos.name)
    
    def test_average_salary(self):
        pos = position_service.get_pos_by_id(1)
        self.assertEqual(1500, position_service.get_avg_salary(pos))
    
    def test_count_emp(self):
        pos = position_service.get_pos_by_id(1)
        self.assertEqual(1, position_service.get_emp_count(pos))
    
    def test_delete(self):
        position_service.delete(4)
        self.assertEqual(3, len(position_service.get_all_pos()))
    