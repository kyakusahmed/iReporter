from datetime import datetime

interventions = []
Redflags = []

class Redflag:
    """class to manipulate red-flags."""

    def __init__(self):
        self.interventions = interventions
        self.redflags = Redflags

    def search_redflag(self, redflag_id):
        """Search specific redflag."""
        search_redflag = [redflag for redflag in self.redflags if redflag['redflag_id'] == redflag_id] 
        return search_redflag

    def get_specific_redflag(self, redflag_id):
        """get one redflag."""
        return self.search_redflag(redflag_id)    

    def delete_redflag(self, redflag_id):
        """remove a specific redflag."""
        search = self.search_redflag(redflag_id)
        if search:
            self.redflags.remove(search[0])
            return "redflag deleted"
        return None   

    def edit_redflag(self, redflag_id, comment):
        """Search redflag and update body and if not found, return None."""
        redflag = self.search_redflag(redflag_id)
        if redflag:
            redflag[0].update({'comment': comment})
            return [{"message": "comment updated", "redflag_id": redflag[0]['redflag_id']}]
        return None    

    def get_all_redflags(self):
        """get list of all red-flags."""
        return self.redflags
      
    def redflag_id(self):
        """get last id increment by 1."""
        if len(self.redflags) < 1:
            return 1
        return self.redflags[-1]['redflag_id'] + 1    

    def create_redflag(self, comment, createdBy, image, location, redflag_id, type, video):
        """create new red-flag."""
        redflag = {
            "comment": comment,
            "createdBy": createdBy,
            "createdOn": str(datetime.now()),
            "image": image,
            "location": location,
            "redflag_id": self.redflag_id(),
            "status": "pending",
            "type": type,
            "video": video
        }
        self.redflags.append(redflag)
        return redflag

    def validate_datatype(self, data_type, data=list):
        """Valdate Data type."""
        for x in data:
            try:
                int(x)
            except ValueError as error:
                return "Sorry {}. please enter an integer value {}".format(str(error), x)
        return None
        



    
                   
