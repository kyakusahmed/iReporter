import unittest
import json
from app.views import app2

class RedflagTest(unittest.TestCase):
    """Tests for Redflag."""

    def setUp(self):
        self.app = app2.test_client()
        self.app.testing = True
    

    def test_post_order(self):
        """Post new order."""
        data_test = {
            "client_id": 7,
            "body": "me and you",
            "location": "bundibugyo"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        assert data["message"] == "redtag added successfully"