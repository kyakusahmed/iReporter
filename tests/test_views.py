import unittest
import json
from app.views import app2

class RedflagTest(unittest.TestCase):
    """Tests for Redflag."""

    def setUp(self):
        self.app2 = app2.test_client()
        self.app2.testing = True

    def test_edit_redflag(self):
        test_data = {"client_id": 1, "body": "ofbuvaboveg", "location": "masaka"}
        self.app2.post('/api/v1/redflags', json=test_data)
        body = {"body": "me and you"}
        response = self.app2.put('/api/v1/redflags/1', json=body)
        self.assertEqual(response.status_code, 404)

    def test_get_specific_redflag(self):
        test_data = {"client_id": 1, "body": "ofbuvaboveg", "location": "masaka"}
        self.app2.post('/api/v1/redflags', json=test_data)
        response = self.app2.get('/api/v1/redflags/1')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(json.loads(response.data.decode('utf-8')).get('test_data')[0]['client_id'], 1)
        # self.assertEqual(json.loads(response.data.decode('utf-8')).get('test_data')[0]['body'], "ofbuvaboveg")
        # self.assertEqual(json.loads(response.data.decode('utf-8')).get('test_data')[0]['location'], "masaka")

    def test_get_all_redtags(self):
        """Test get all redflags."""
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
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        assert data["message"] == "redflag added successfully"

