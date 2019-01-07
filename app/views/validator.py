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