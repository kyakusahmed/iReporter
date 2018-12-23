from flask import request

message = []
input_data = []

class Validation:
    """class for validating data"""
    def __init__(self):
        self.message = message

    def validate_datatype(self, data_type, input_data):
        """search for x and validate data type."""
        for x in input_data:
            try:
                int(x)
            except ValueError as error:
                return "Sorry {}. please enter an integer value {}".format(str(error), x)
        return None

    def input_data_validation(self, input_data):
        """Search for input x and check for empty string."""
        for x in input_data:
            input = request.get_json()
            input[x]
            if not input[x]:
                self.message.append('missing field')
                return self.message 

             
        
    