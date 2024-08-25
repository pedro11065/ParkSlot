from flask import Blueprint, request, jsonify
from src.model.entry.verification_entry import v_entry
from ParkSlot.src.model.database.db_delete_car import db_delete

api_car_exit = Blueprint('api_car_exit', __name__)

@api_car_exit.route('/api/exit', methods=['POST'])
def exit():

#--------------------------------------------------------------------ENTRY

    car_data = request.get_json() 

#--------------------------------------------------------------------PROCESS

    data_v_exit = [car_data['placa'], car_data['nomecliente']]

    v_exit(data_v_exit) #verification_entry

#--------------------------------------------------------------------RETURN

    if data_v_exit == True:

        db_delete(data_v_exit)
        return jsonify({"placa": "True"}), 200
    
    else:
        
        return jsonify({"placa": "False"}), 400

