import sys

def add():

    sys.path.append('C:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/view')
    from v_global_functions.clear_terminal import clean_terminal

    clean_terminal()

    plate = input("Car plate:")
    Cname = input("Custumer's first name:")

    clean_terminal()

    return plate,Cname



