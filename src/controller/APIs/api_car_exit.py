from flask import Blueprint, request, jsonify
from src.model.exit.verification_exit import v_exit
from src.model.database.db_delete_car import db_delete


api_car_exit = Blueprint('car_exit', __name__)

@api_car_exit.route('/exit', methods=['POST'])
def exit():

#--------------------------------------------------------------------ENTRY

    car_data = request.get_json() 

#--------------------------------------------------------------------PROCESS

    data_v_exit = [car_data['placa'], car_data['nomecliente']]

    exit = v_exit(data_v_exit) #verification_exit

#--------------------------------------------------------------------RETURN
    
    if exit == False:
        
        return jsonify({"placa": "False"}), 400
    
    db_delete(exit)
    return jsonify({"Exit": "True", "Value": exit[1]}), 200
