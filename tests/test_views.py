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