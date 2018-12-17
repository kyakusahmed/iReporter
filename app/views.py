
from flask import Flask, jsonify, request
from app.redflag import Redflag

app2 = Flask(__name__)
Redflag = Redflag()

@app2.route('/api/v1/redflags/<int:id>', methods=['DELETE'])
def delete_redflag(id):
    search = Redflag.search_redflag(id)
    if not search:
        return jsonify({"message":"unable to find redflag"}), 404

    delete_redflag = Redflag.delete_redflag(id)
    if delete_redflag:
        return jsonify({"message": "redflag deleted is successful"}), 200
    return jsonify({"error", "failed to delete redflag"}), 200

@app2.route('/api/v1/redflags/<int:id>', methods=["PUT"])
def edit_redflag(id):
    get_input = request.get_json()
    if not get_input.get("body"):
        return jsonify({"error" : "body is required"}), 200
    edit_redflag = Redflag.edit_redflag(id, get_input['body'])
    if edit_redflag:
        return jsonify({"redflag":edit_redflag}), 200
    return jsonify({"message":"unable to find redflag"}), 404

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

@app2.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    data = request.get_json()
    if not data.get("client_id"):
        return jsonify({"error": "client_id is required"}), 200
    elif not data.get("body"):
        return jsonify({"error": "body is required"}), 200
    elif not data.get('location'):
        return jsonify({"error": "location is required"}), 200
    return jsonify({"message": Redflag.create_redflag(id, data["client_id"], data["body"], data["location"]), "status": 201})


