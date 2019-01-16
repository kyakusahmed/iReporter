"""Manage redflags."""
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
        search = [
            item for item in self.redflags if item['redflag_id'] == redflag_id]
        return search

    def get_specific_redflag(self, redflag_id):
        """get one redflag."""
        return self.search_redflag(redflag_id)

    def delete_redflag(self, redflag_id):
        """remove a specific redflag."""
        search = self.search_redflag(redflag_id)
        if search:
            self.redflags.remove(search[0])
            return "redflag deleted"

    def edit_redflag(self, redflag_id, comment):
        """Search redflag and update body and if not found, return None."""
        redflag = self.search_redflag(redflag_id)
        if redflag:
            redflag[0].update({'comment': comment})
            return [{
                "message": "comment updated",
                "redflag_id": redflag[0]['redflag_id']
                }]
        return None

    def get_all_redflags(self):
        """get list of all red-flags."""
        return self.redflags

    def add_redflag(self, comment, createdby, fromMyCamera, location):
        """create new red-flag."""
        redflag = {
            "comment": comment,
            "createdby": createdby,
            "createdOn": str(datetime.now()),
            "fromMyCamera": fromMyCamera,
            "location": location,
            "redflag_id": len(self.redflags)+1,
            "status": "pending",
            "type": "redflag",
        }
        self.redflags.append(redflag)
        return redflag
