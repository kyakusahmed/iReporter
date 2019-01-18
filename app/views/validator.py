from flask import request

message = []
incidents = []
class Validation:
    """class for validating data"""
    def __init__(self):
        self.message = message
        self.incidents = incidents

    def input_data_validation(self, incidents):
        """Search for x and check if data is an empty string."""
        for x in incidents:
            data = request.get_json()
            if not data[x]:
                self.message.append('missing field')
                return self.message

    def validate_location(self, location):
        data = request.get_json()
        location = data['location'].split(',')

        try:
            lat = float(location[0])
            lng = float(location[1])

            if len(location) != 2:
                return "invalid coordinates" 
            elif not (lat >= -90 and lat <= 90):
                return 'latitude out of range is'
            elif not (lng >= -180 and lng <= 180):
                return 'longtude is out of range'
        except ValueError:
            return "please enter numbers and not a letter"
        except IndexError:
            return "either latitude or longtude is missing"    