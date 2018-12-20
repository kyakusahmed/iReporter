from flask import Flask, jsonify, request
from app.redflag import Redflag

app2 = Flask(__name__)
Redflag = Redflag()


@app2.route('/', methods=['GET'])
def index():
    """opening route."""
    return jsonify({'message': 'welcome to iReporter.'}), 200


@app2.route('/api/v1/redflags/<int:id>/edit', methods=["PUT"])
def edit_redflag(id):
    """edit a specific redflag"""
    get_input = request.get_json()
    if not get_input.get("body"):
        return jsonify({"error": "body is required"}), 200
    edit = Redflag.edit_redflag(id, get_input['body'])
    if edit:
        return jsonify({"redflag": edit}), 200
    return jsonify({"message": "unable to find redflag"}), 404

@app2.route('/api/v1/redflags/<int:id>/one', methods=['GET'])
def get_specific_redflag(id):
    """get a specific redflag"""
    redflag1 = Redflag.get_specific_redflag(id)
    print('redflag')
    if redflag1:
        return jsonify({"redflag": redflag1}), 200
    return jsonify({"message": "redflag not found"}), 404
  
@app2.route('/api/v1/redflags', methods=['GET'])    
def get_all_redflags():
    """fetch all redflags"""
    redflags = Redflag.get_all_redflags()
    return jsonify({"redflags": redflags}), 200


@app2.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    """add redflag to self.redflags"""
    data = request.get_json()
    validate_datatype = Redflag.validate_datatype(int, [data['client_id']])
    if validate_datatype:
        return jsonify({"data_type_error": validate_datatype}), 200
    if not data.get("client_id"):
        return jsonify({"error": "client_id is required"}), 200
    elif not data.get("body"):
        return jsonify({"error": "body is required"}), 200
    elif not data.get('location'):
        return jsonify({"error": "location is required"}), 200
    return jsonify({"message": Redflag.create_redflag(
        id, data["client_id"], data["body"], data["location"])}), 201


@app2.route('/api/v1/redflags/<int:id>/delete', methods=['DELETE'])
def delete_redflag(id):
    """remove item from self.redflags"""
    search = Redflag.search_redflag(id)
    if not search:
        return jsonify({"message": "unable to find redflag"}), 404
    delete = Redflag.delete_redflag(id)
    if delete:
        return jsonify({"message": "redflag deleted is successful"}), 200
    return jsonify({"error", "failed to delete redflag"}), 200    

    


