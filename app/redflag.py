from datetime import datetime

interventions = []
redflags = []

class Redflag:

    """class to manipulate red-flags."""

    def __init__(self):
        self.interventions = interventions
        self.redflags = redflags

    def get_all_redflags(self):
        """get list of all red-flags."""
        return self.redflags