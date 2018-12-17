from datetime import datetime

interventions = []
redflags = []

class Redflag:

    def __init__(self):
        self.interventions = interventions
        self.redflags = redflags

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

    
