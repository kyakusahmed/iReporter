import unittest
import json
from app.views import app2

class RedflagTest(unittest.TestCase):
    """Tests for Redflag."""

    def setUp(self):
        self.app2 = app2.test_client()
        self.app2.testing = True

    def test_delete_redflag(self):
        test = {
            "client_id": 7,
            "body": "me and you",
            "location": "bundibugyo"
        }
        self.app2.post('/api/v1/redflags', json=test)
        response = self.app2.delete('/api/v1/redflags/1/delete')
        self.assertEqual(response.status_code, 200)


    def test_edit_redflag(self):
        test_data = {"client_id": 1, "body": "ofbuvaboveg", "location": "masaka"}
        self.app2.post('/api/v1/redflags', json=test_data)
        body = {"body": "me and you"}
        response = self.app2.put('/api/v1/redflags/1/edit', json=body)
        self.assertEqual(response.status_code, 200)

    def test_get_specific_redflag(self):
        test_data = {"client_id": 1, "body": "ofbuvaboveg", "location": "masaka"}
        self.app2.post('/api/v1/redflags', json=test_data)
        response = self.app2.get('/api/v1/redflags/1/one')
        self.assertEqual(response.status_code, 200)

    def test_get_all_redtags(self):
        """Test get all redflags."""
        data_test = {
            "client_id": 7,
            "body": "me and you",
            "location": "bundibugyo"
        }
        response = self.app2.post('/api/v1/redflags', json=data_test)
        response = self.app2.get('/api/v1/redflags')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data.decode('utf-8')).get('redflags'), list)
   
    def test_create_redflag(self):
        """Post new redflag."""
        data_test = {
            "client_id": 7,
            "body": "me and you",
            "location": "bundibugyo"
        }
        response = self.app2.post('/api/v1/redflags', json=data_test)
        self.assertEqual(response.status_code, 201)


    


  
       
        
     


