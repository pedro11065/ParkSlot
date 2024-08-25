from flask import Blueprint, request, jsonify
from src.model.entry.verification_entry import v_entry
from src.model.database.db_register_car import db_register_car

api_car_entry = Blueprint('api_car_entry', __name__)

@api_car_entry.route('/api/entry', methods=['POST'])
def login():

#--------------------------------------------------------------------ENTRY

    car_data = request.get_json() 

#--------------------------------------------------------------------PROCESS

    data_v_entry = [car_data['placa'], car_data['nomecliente']]

    v_entry(data_v_entry) #verification_entry

#--------------------------------------------------------------------RETURN

    if data_v_entry == True:

        db_register_car(data_v_entry)
        return jsonify({"placa": "True"}), 200
    
    else:
        
        return jsonify({"placa": "False"}), 400

