from flask import Flask, jsonify, request
from app.redflag import Redflag

app2 = Flask(__name__)
Redflag = Redflag()


@app2.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    data = request.get_json()
    if not data.get("client_id"):
        return jsonify({"error": "client_id is required"}), 200
    elif not data.get("body"):
        return jsonify({"error": "body is required"}), 200
    elif not data.get('location'):
        return jsonify({"error": "location is required"}), 200
    return jsonify({"message": Redflag.create_redflag(id, data["client_id"], data["body"], data["location"])}), 201
