
import unittest
from department_app import app

client = app.test_client()

class TestEmployeeView(unittest.TestCase):
    
    def test_employees(self):
        res = client.get('/employees/')
        self.assertEqual(res.status_code, 200)
    
    def test_add_employees(self):
        res = client.get('/add_employee')
        self.assertEqual(res.status_code, 200)
    
    def test_delete_employee(self):
        res = client.get('/employees/delete/1')
        self.assertEqual(res.status_code, 302)
