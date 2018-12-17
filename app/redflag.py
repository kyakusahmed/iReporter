from datetime import datetime

interventions = []
redflags = []

class Redflag:
    """class to manipulate red-flags."""

    def __init__(self):
        self.interventions = interventions
        self.redflags = redflags

    def search_redflag(self, id):
        """Search specific redflag."""
        redflag = [redflag for redflag in self.redflags if redflag['id'] == int(id)] 
        return redflag   

        

    