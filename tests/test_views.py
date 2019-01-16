import unittest
import json
from app.views.views import app

class RedflagTest(unittest.TestCase):
    """Tests for Redflag."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_delete_redflag(self):
        test = {
            "createdby": 1,
            "location": "90,112",
            "fromMyCamera": "dasfrg",
            "comment":"AVNNDICV"
        }
        self.app.post('/api/v1/redflags', json=test)
        response = self.app.delete('/api/v1/redflags/1/delete')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('message'), "redflag deleted is successful")
        

    def test_delete_redflag_not_found(self):
        response = self.app.delete('/api/v1/redflags/1000/delete')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('error'), "unable to find redflag")


    def test_edit_redflag_flag_not_found(self):
        body = {"comment": "me and you"}
        response = self.app.patch('/api/v1/redflags/1000/edit', json=body)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('error'), "unable to find redflag")


    def test_edit_redflag_flag_comment_missing(self):
        test_data = {
            "comment": "",
            "createdby": 1,
            "image": "image",
            "location": "location",
            "status": "pending",
            "type": "redflag",
            "video": "video"
            }
        self.app.post('/api/v1/redflags', json=test_data)
        body = {
            "comment": ""
            }
        response = self.app.patch('/api/v1/redflags/2/edit', json=body)
        self.assertEqual(response.status_code, 400)


    def test_edit_redflag_flag(self):
        test_data = {
            "createdby": 1,
            "location": "90,112",
            "fromMyCamera": "dasfrg",
            "comment":"AVNNDICV"
            }
        self.app.post('/api/v1/redflags', json=test_data)
        body = {
            "comment": "me and you"
            }
        response = self.app.patch('/api/v1/redflags/2/edit', json=body)
        self.assertEqual(response.status_code, 200)


    def test_get_specific_redflag_not_found(self):
        test_data = {"client_id": 1, "body": "ofbuvaboveg", "location": "masaka"}
        self.app.post('/api/v1/redflags', json=test_data)
        response = self.app.get('/api/v1/redflags/100/one')
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('error'), "redflag not found")
        self.assertEqual(response.status_code, 404)


    def test_get_specific_redflag(self):
        test_data = {
            "createdby": 1,
            "location": "90,112",
            "fromMyCamera": "dasfrg",
            "comment": "vkA"
            }
        self.app.post('/api/v1/redflags', json=test_data)
        response = self.app.get('/api/v1/redflags/2/one')
        self.assertEqual(response.status_code, 200)

    def test_get_all_redtags(self):
        """Test get all redflags."""
        data_test = {
            "client_id": 7,
            "body": "me and you",
            "location": "bundibugyo"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        response = self.app.get('/api/v1/redflags')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data.decode('utf-8')).get('redflags'), list)
   
    def test_add_redflag(self):
        """test add new redflag."""
        data_test = {
            "createdby": 1,
            "location": "90,112",
            "fromMyCamera": "dasfrg",
            "comment":"AVNNDICV"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(json.loads(response.data.decode('utf-8')).get('data'), list)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('data')[0]['message'], "redflag added successfully")


    def test_opening_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('message'), "welcome to iReporter.")
        
    def test_add_redflag_location_is_required(self):
        data_test = {
            "comment": "covbwcwuob",
            "createdby": 1,
            "image": "image",
            "location": "",
            "type": "redflag",
            "video": "baiowqgb"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('error'), "missing field")

    def test_add_redflag_comment_is_required(self):
        data_test = {
            "createdby": 1,
            "location": "90,112",
            "fromMyCamera": "dasfrg",
            "comment":""
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('error'), "missing field")


    def test_data_type_entered_is_not_integer(self):
        """test add new redflag."""
        data_test = {
            "createdby": "vds",
            "location": "90,112",
            "fromMyCamera": "dasfrg",
            "comment":"cfjisldf"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(
            response.data.decode('utf-8')).get("data_type_error"),
            "Sorry invalid literal for int() with base 10: 'vds'. please enter an integer value vds"
            )