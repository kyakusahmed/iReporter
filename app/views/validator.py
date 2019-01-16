from flask import request

message = []
incidents = []
class Validation:
    """class for validating data"""
    def __init__(self):
        self.message = message
        self.incidents = incidents

    def validate_datatype(self, data_type, incidents):
        """search for x and validate data type."""
        for x in incidents:
            try:
                int(x)
            except ValueError as error:
                return "Sorry {}. please enter an integer value {}".format(str(error), x)
        return None

    def input_data_validation(self, incidents):
        """Search for x and check if input is an empty string."""
        for x in incidents:
            data = request.get_json()
            if not data[x]:
                self.message.append('missing field')
                return self.message

    def validate_location(self, location):
        input = request.get_json()
        location = input['location'].split(',')

        try:
            lat = float(location[0])
            lng = float(location[1])

            if len(location) != 2:
                return "invalid coordinates"
            elif not location[0] or not location[1]:
                return "either latitude or longtude field is missing"
            elif not (lat >= -90 and lat <= 90):
                return 'latitude is out of range'
            elif not (lng >= -180 and lng <= 180):
                return 'longtude is out of range'
        except ValueError:
            return "pliz enter numbers and not a letter"            
                

    