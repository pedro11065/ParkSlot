from flask import Blueprint, request, jsonify
from src.model.entry.verification_entry import v_entry
from src.model.database.db_register_car import database_create

api_car_entry = Blueprint('car_entry', __name__)

@api_car_entry.route('/entry', methods=['POST'])
def login():

#--------------------------------------------------------------------ENTRY

    car_data = request.get_json() 

#--------------------------------------------------------------------PROCESS

    car_data = [car_data['plate'], car_data['custumer_name']]
    plate = car_data[0]
    custumer_name = car_data[1]

    data_v_entry = v_entry(plate) #verification_entry

#--------------------------------------------------------------------RETURN

    if data_v_entry == True:

        entry, error = database_create(plate,custumer_name)

        if entry:

            return jsonify({"plate": True,"Server": True, "Error": error}), 200
        
        return jsonify({"plate": True,"Server": False, "Error": error}), 502
    
    else:
        
        return jsonify({"plate": False, "Server": False, "Error": "Plate isen't in database" }), 400

