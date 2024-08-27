from flask import Blueprint, request, jsonify
from src.model.entry.verification_entry import v_entry
from src.model.database.db_register_car import database_create

api_car_entry = Blueprint('car_entry', __name__)

@api_car_entry.route('/entry', methods=['POST'])
def login():

#--------------------------------------------------------------------ENTRY

    car_data = request.get_json() 

#--------------------------------------------------------------------PROCESS

    car_data = [car_data['placa'], car_data['nomecliente']]

    data_v_entry = v_entry(car_data) #verification_entry

#--------------------------------------------------------------------RETURN

    if data_v_entry == True:

        if database_create(car_data):

            return jsonify({"placa": "True","Server": "True"}), 200
        
        return jsonify({"placa": "True","Server": "False"}), 400
    
    else:
        
        return jsonify({"placa": "False"}), 400

