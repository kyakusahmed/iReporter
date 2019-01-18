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
    return jsonify({
        "status": 200, 'message': 'welcome to iReporter.'
        }), 200


@app.route('/api/v1/redflags/<int:redflag_id>/edit', methods=["PATCH"])
def edit_redflag(redflag_id):
    """edit a specific redflag"""
    input_data = request.get_json()
    if not input_data.get("comment"):
        return jsonify({"error": "comment is required", "status": 400}), 400
    edit = record.edit_redflag(redflag_id, input_data['comment'])
    if not edit:
        return jsonify({
            "error": "unable to find redflag", "status": 404
            }), 404
    return jsonify({
        "redflag": edit, "status": 200
        }), 200


@app.route('/api/v1/redflags/<int:redflag_id>/one', methods=['GET'])
def get_specific_redflag(redflag_id):
    """get a specific redflag"""
    redflag = record.get_specific_redflag(redflag_id)
    if not redflag:
        return jsonify({
            "error": "redflag not found", "status": 404
            }), 404
    return jsonify({
        "status": 200, "redflag": redflag
        }), 200


@app.route('/api/v1/redflags', methods=['GET'])
def get_all_redflags():
    """fetch all redflags"""
    redflags = record.get_all_redflags()
    return jsonify({
        "redflags": redflags, "status": 200
        }), 200


@app.route('/api/v1/redflags', methods=['POST'])
def add_redflag():
    """add redflag to self.redflags"""
    input_validation = validation.input_data_validation([
        "comment",
        "location",
        "type",
        "createdby"
        ])
    if input_validation:
        return jsonify({"status": 400, "error": input_validation[0]}), 400

    data = request.get_json()
    if type(data['createdby']) is not int:
        return jsonify({
            "data_type_error": "please enter an integer",
            "status": 400
            }), 400

    validate_location = validation.validate_location(data['location'])
    if validate_location:
        return jsonify({
            "location_validation": validate_location, "status": 400
            }), 400

    incident_type = data['type']
    incident_types = ['redflag', 'intervention']
    if incident_type not in incident_types:
        return jsonify({
            "status": 400, "error": " incident_type {} doesnot exist".format(incident_type)}), 400        

    incident = record.add_redflag(
        data['comment'],
        data["createdby"],
        data['image'],
        data["location"],
        data['type'],
        data['video']
        )
    red_flag = [{
        "redflag_id": incident['redflag_id'],
        "message": "redflag added successfully"
        }]
    return jsonify({"data": red_flag, "status": 201}), 201


@app.route('/api/v1/redflags/<int:redflag_id>/delete', methods=['DELETE'])
def delete_redflag(redflag_id):
    """remove item from self.redflags"""
    search = record.search_redflag(redflag_id)
    if not search:
        return jsonify({
            "error": "unable to find redflag", "status": 404
            }), 404
    delete = record.delete_redflag(redflag_id)
    if delete:
        return jsonify({
            "status": 200,
            "message": "redflag deleted is successful"
            }), 200
