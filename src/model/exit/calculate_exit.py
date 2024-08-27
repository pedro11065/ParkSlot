def total_to_pay(entry_time,entry_data):

    from src.model.time import time_now

    now_data = time_now()[0]
    now_time = time_now()[1]

    entry_data == now_data

    entry_time_ = entry_time
    entry_time_ = entry_time.split(":")
    now_time = now_time.split(":")

    entry_time_ = int(entry_time_[0]) + (entry_time_[1])
    now_time = int(now_time[0]) + (now_time[1])

    time_in_parking = int(now_time) - int(entry_time_)
    value = time_in_parking * 10 #Preço da hora

    return value




