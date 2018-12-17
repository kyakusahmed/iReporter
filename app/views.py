from flask import Flask, jsonify, request
from app.redflag import Redflag

app2 = Flask(__name__)
Redflag = Redflag()

@app2.route('/api/v1/redflags/<int:id>', methods=['GET'])
def get_specific_redflag(id):
    redflag = Redflag.search_redflag(id)
    print(redflag)
    if not redflag:
        return({"message":"redflag not found"}), 404
    return jsonify({"status": 200, "redflag": {'id':redflag[0],
                                'client_id':redflag[1],
                                'body':redflag[2],
                                'location':redflag[3],
                                'status':redflag[4],
                                'created_at':redflag[5]}})


                                

  