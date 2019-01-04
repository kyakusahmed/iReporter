from flask import request

message = []
data = []

class Validation:
    """class for validating data"""
    def __init__(self):
        self.message = message

    def validate_datatype(self, data_type, data):
        """search for x and validate data type."""
        for x in data:
            try:
                int(x)
            except ValueError as error:
                return "Sorry {}. please enter an integer value {}".format(str(error), x)
        return None

    def input_data_validation(self, data):
        """Search for x and check if input is an empty string."""
        for x in data:
            input = request.get_json()
            if not input[x]:
                self.message.append('missing field')
                return self.message 