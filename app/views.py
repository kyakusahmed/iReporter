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

