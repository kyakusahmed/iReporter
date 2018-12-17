import unittest
import json
from app.views import app2

class RedflagTest(unittest.TestCase):
    """Tests for Redflag."""

    def setUp(self):
        self.app2 = app2.test_client()
        self.app2.testing = True

    def test_delete_redflag(self):
        """delete redflag."""
        data_test = {
            "client_id": 7,
            "body": "me and you",
            "location": "bundibugyo"
        }
        self.app2.post('/api/v1/redflags', json=data_test)
        response = self.app2.delete('/api/v1/redflags/1')
        data = json.loads(response.get_data(as_text=True))
        assert data["message"] == "unable to find redflag" 
       
        
     