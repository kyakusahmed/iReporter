"""all the endpoints"""
from flask import Flask, jsonify, request
from app.models.redflag import Redflag
from app.views.validator import Validation

app = Flask(__name__)
record = Redflag()
validation = Validation()


@app.route('/', methods=['GET'])
def index():
    """opening route."""
    return jsonify({"status": 200, 'message': 'welcome to iReporter.'}), 200


@app.route('/api/v1/redflags/<int:redflag_id>/edit', methods=["PATCH"])
def edit_redflag(redflag_id):
    """edit a specific redflag"""
    input_data = request.get_json()
    if not input_data.get("comment"):
        return jsonify({"error": "comment is required", "status": 400}), 400
    edit = record.edit_redflag(redflag_id, input_data['comment'])
    if not edit:
        return jsonify({"error": "unable to find redflag", "status": 404}), 404
    return jsonify({"redflag": edit, "status": 200}), 200
    

@app.route('/api/v1/redflags/<int:redflag_id>/one', methods=['GET'])
def get_specific_redflag(redflag_id):
    """get a specific redflag"""
    redflag = record.get_specific_redflag(redflag_id)
    if not redflag:
        return jsonify({"error": "redflag not found", "status": 404}), 404
    return jsonify({"status": 200, "redflag": redflag}), 200
   
  
@app.route('/api/v1/redflags', methods=['GET'])    
def get_all_redflags():
    """fetch all redflags"""
    redflags = record.get_all_redflags()
    return jsonify({"redflags": redflags, "status": 200}), 200
    

@app.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    """add redflag to self.redflags"""
    input_validation = validation.input_data_validation(["comment", "location", "type"])
    if input_validation:
        return jsonify({"status": 400, "error": input_validation[0]}), 400

    data = request.get_json()
    validate_datatype = validation.validate_datatype(int, [data['createdBy']])
    if validate_datatype:
        return jsonify({"data_type_error": validate_datatype, "status": 400}), 400

    record_type = data['type'] 
    record_types = ['redflag', 'interventions'] 
    if record_type not in record_types:
        return jsonify({"error": "record_type {} doesnot exist".format(record_type), "status": 400}), 400

    incident = record.create_redflag("redflag_id", data["createdBy"], data['type'], 
    data["location"], data['image'], data['video'], data['comment'])

    red_flag = [{"redflag_id": incident['redflag_id'], "message": "redflag added successfully"}]
    return jsonify({"data": red_flag, "status": 201}), 201


@app.route('/api/v1/redflags/<int:redflag_id>/delete', methods=['DELETE'])
def delete_redflag(redflag_id):
    """remove item from self.redflags"""
    search = record.search_redflag(redflag_id)
    if not search:
        return jsonify({"error": "unable to find redflag", "status": 400}), 400
    delete = record.delete_redflag(redflag_id)
    if delete:
        return jsonify({"status": 200, "message": "redflag deleted is successful"}), 200
    return jsonify({"status": 400, "error": "failed to delete redflag"}), 400   

    


