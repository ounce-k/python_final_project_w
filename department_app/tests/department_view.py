import unittest
from department_app import app

client = app.test_client()

class TestDepartmentView(unittest.TestCase):
    
    def test_departments(self):
        res = client.get('/departments/')
        self.assertEqual(res.status_code, 200)
    
    def test_add_departments(self):
        res = client.get('/add_department')
        self.assertEqual(res.status_code, 200)
    
    def test_delete_department(self):
        res = client.get('/departments/delete/1')
        self.assertEqual(res.status_code, 302)

    def test_get_department(self):
        res = client.get('/departments/1')
        self.assertEqual(res.status_code, 200)  