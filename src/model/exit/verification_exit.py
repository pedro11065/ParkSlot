def v_exit(data_v_exit):

    from src.model.database.db_search_car import db_search
    from src.model.exit.calculate_exit import total_to_pay

    search_data = data_v_exit[0] 
     # 0     1         2             3              4
    db_data = db_search(search_data) #id, plate, custumer_name, time_arrive, date_arrive

    if db_data == False:
        return False
    
    else:
        entry_time = db_data[1][0][3]
        entry_data = db_data[1][0][4]

        value = total_to_pay(entry_time,entry_data)

        #        0     1        2         3          4          5           6
        return True, value, 

        


    