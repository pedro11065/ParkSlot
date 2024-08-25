def v_exit(data_v_exit):

    from src.model.database.db_search_car import db_search
    
    search_data = data_v_exit[0]

    if db_search(search_data):
        return True
    return False