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
        