
from flask import Flask, jsonify, request
from app.redflag import Redflag

app2 = Flask(__name__)

Redflag = Redflag()

@app2.route('/api/v1/redflags/<int:id>', methods=["PUT"])
def edit_redflag(id):
    get_input = request.get_json()
    if not get_input.get("body"):
        return jsonify({"error" : "body is required"}), 200
    edit_redflag = Redflag.edit_redflag(id, get_input['body'])
    if edit_redflag:
        return jsonify({"redflag":edit_redflag}), 200
    return jsonify({"message":"unable to find redflag"}), 404


