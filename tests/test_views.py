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
            "comment": "hey boss, u dont have to give money to do for u this",
            "createdBy": 1,
            "image": "image",
            "location": "location",
            "type": "redflag",
            "video": "baiowqgb"
        }
        self.app.post('/api/v1/redflags', json=test)
        response = self.app.delete('/api/v1/redflags/1/delete')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        assert data["message"] == "redflag deleted is successful"
        

    def test_delete_redflag_not_found(self):
        response = self.app.delete('/api/v1/redflags/1000/delete')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400) 
        assert data['error'] == "unable to find redflag"


    def test_edit_redflag_flag_not_found(self):
        body = {"comment": "me and you"}
        response = self.app.patch('/api/v1/redflags/1000/edit', json=body)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data.decode('utf-8')).get('error'), "unable to find redflag")


    def test_get_specific_redflag_not_found(self):
        test_data = {"client_id": 1, "body": "ofbuvaboveg", "location": "masaka"}
        self.app.post('/api/v1/redflags', json=test_data)
        response = self.app.get('/api/v1/redflags/100/one')
        data = json.loads(response.get_data(as_text=True))
        assert data["error"] == "redflag not found"
        self.assertEqual(response.status_code, 404)

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
   
    def test_create_redflag(self):
        """test add new redflag."""
        data_test = {
            "comment": "abehtjtuk",
            "createdBy": 1,
            "image": "image",
            "location": "location",
            "type": "redflag",
            "video": "baiowqgb"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(json.loads(response.data.decode('utf-8')).get('data'), list)
        assert data['data'][0]['message'] == "redflag added successfully"


    def test_opening_route(self):
        response = self.app.get('/')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        assert data["message"] == "welcome to iReporter."

    def test_create_redflag_location_is_required(self):
        data_test = {
            "comment": "covbwcwuob",
            "createdBy": 1,
            "image": "image",
            "location": "",
            "type": "redflag",
            "video": "baiowqgb"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        assert data["error"] == "missing field"

    def test_create_redflag_comment_is_required(self):
        data_test = {
            "comment": "",
            "createdBy": 1,
            "image": "image",
            "location": "location",
            "type": "",
            "video": "baiowqgb"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        assert data['error'] == "missing field"

    def test_create_redflag_type_is_required(self):
        data_test = {
            "comment": "hey boss, u dont have to give money to do for u this",
            "createdBy": 1,
            "image": "image",
            "location": "location",
            "type": "",
            "video": "baiowqgb"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        assert data["error"] == "missing field"

    def test_data_type_entered_is_not_integer(self):
        """test add new redflag."""
        data_test = {
            "comment": "abehtjtuk",
            "createdBy": "",
            "image": "image",
            "location": "location",
            "type": "redflag",
            "video": "baiowqgb"
        }
        response = self.app.post('/api/v1/redflags', json=data_test)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        assert data["data_type_error"] == "Sorry invalid literal for int() with base 10: ''. please enter an integer value "


    def test_record_type_doesnot_exist(self):
        test_data = {
            "comment": "abehtjtuk",
            "createdBy": 1,
            "image": "image",
            "location": "location",
            "type": "aefbtnw",
            "video": "baiowqgb"
        }
        response = self.app.post('/api/v1/redflags', json=test_data)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        assert data["error"] == "record_type aefbtnw doesnot exist"

      


    
        


       

       
    
            




    


  
       
        
     


