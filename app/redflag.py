
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
        return redflag   

    def edit_redflag(self, id, body):
        """Search redflag and update body and if not found, return None."""
        Redflag = self.search_redflag(id)
        if Redflag:
            Redflag[0].update({'body': body})
            return "body updated successfully"
        return None

    def get_all_redflags(self):
        """get list of all red-flags."""
        return self.redflags
      
    def id(self):
        """get last id increment by 1."""
        if len(self.redflags) < 1:
            return 1
        return self.redflags[-1]['id'] + 1    

    def create_redflag(self, id, client_id, body, location):
        """create new red-flag."""
        redflag = {
            "id": self.id(),
            "client_id": client_id,
            "body": body,
            "location": location,
            "status": "pending",
            "created_at": str(datetime.now())
        }
        self.redflags.append(redflag)
        return "redflag added successfully"



