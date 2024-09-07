def v_exit(plate,custumer_name,first_hour,next_hours,day):

    from src.model.database.db_search_car import db_search
    from src.model.exit.calculate_exit import total_to_pay

    search_data = plate
     # 0     1         2             3              4
    car, db_data = db_search(search_data) #id, plate, custumer_name, time_arrive, date_arrive

    if car == False:
        return False, None, None, None, db_data
    
    entry_time = db_data.get('entry_time')
    entry_date = db_data.get('entry_data')
    first_hour_price = int(first_hour)
    next_hours_price = int(next_hours)
    day_price = int(day)


    to_pay = total_to_pay(entry_time,entry_date,first_hour_price,next_hours_price,day_price)

    #        0     1        2         3          4          5           6
    return True, to_pay, entry_time, entry_date, None

        


    