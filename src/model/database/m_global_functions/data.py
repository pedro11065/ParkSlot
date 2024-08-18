from time import strftime

def data_time():

    data_M = (strftime(" %d/%b/%Y")) #date by month ("day/month/year")
    data_H = (strftime("%H:%M")) #data by hour (hour/minutes)

    return data_M,data_H

print(data_time()[0])
print(data_time()[1])