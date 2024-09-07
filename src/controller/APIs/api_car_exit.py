from flask import Blueprint, request, jsonify
from src.model.exit.verification_exit import v_exit
from src.model.database.db_delete_car import db_delete


api_car_exit = Blueprint('car_exit', __name__)

@api_car_exit.route('/exit', methods=['POST'])
def exit():

#--------------------------------------------------------------------ENTRY

    car_data = request.get_json() 

#--------------------------------------------------------------------PROCESS

    data_v_exit = [car_data['plate'], 
    car_data['custumer_name'], 
    car_data['first_hour'], 
    car_data['next_hours'],
    car_data['day']]
    
    plate = data_v_exit[0]
    custumer_name = data_v_exit[1]
    first_hour = data_v_exit[2]
    next_hours = data_v_exit[3]
    day = data_v_exit[4]
    
    exit, to_pay, entry_time, entry_date, error = v_exit(plate,custumer_name,first_hour,next_hours,day) #verification_exit

#--------------------------------------------------------------------RETURN
    
    if exit == True: 
        
        if db_delete(plate, custumer_name, entry_time, entry_date, to_pay):

            return jsonify({"Exit": True,
                            "placa": True, 
                            "Value": to_pay, 
                            "Server": True, 
                            "Error": error}), 200
        
        return jsonify({"Exit": False ,
                        "placa": True,
                        "Value": "---",
                        "Server": False, 
                        "Error": error}), 502
    
    return jsonify({"Exit": False ,
                    "placa": False, 
                    "Server": False, 
                    "Error": "Car isen't registered"}), 400
