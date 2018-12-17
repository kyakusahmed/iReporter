import unittest
import json
from app.views import app2

class RedflagTest(unittest.TestCase):
    """Tests for Redflag."""

    def setUp(self):
        self.app2 = app2.test_client()
        self.app2.testing = True

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
        response = self.app.post('/api/v1/redflags', json=data_test)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        assert data["message"] == "redflag added successfully"
