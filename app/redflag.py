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

    def delete_redflag(self, id):
        search = self.search_redflag(id)
        if search:
            self.redflags.remove(search[0])
            return "redflag deleted"
