import unittest
from department_app import app

client = app.test_client()

class TestPositionView(unittest.TestCase):
    
    def test_positions(self):
        res = client.get('/positions/')
        self.assertEqual(res.status_code, 200)
    
    def test_add_positions(self):
        res = client.get('/add_position')
        self.assertEqual(res.status_code, 200)
    
    def test_delete_position(self):
        res = client.get('/positions/delete/5')
        self.assertEqual(res.status_code, 302)

    def test_get_position(self):
        res = client.get('/positions/1')
        self.assertEqual(res.status_code, 200)  