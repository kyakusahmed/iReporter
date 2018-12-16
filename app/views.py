from flask import Flask, jsonify, request
from app.redflag import Redflag

app2 = Flask(__name__)
Redflag = Redflag()

@app2.route('/api/v1/redflags', methods=['GET'])    
def get_all_user_redflags():
    redflags = Redflag.get_all_redflags()
    new_list = []
    for key in range(len(redflags)):
        new_list.append({   
                'id':redflags[key][0],
                'client_id':redflags[key][1],
                'sender_name':redflags[key][2],
                'sender_phone':redflags[key][3],
                'pickup_location':redflags[key][4],
                'recepient_name':redflags[key][5],
                'recepient_phone':redflags[key][6],
                'recepient_country':redflags[7]
            })
    return jsonify({"status": 200, "redflags": new_list})