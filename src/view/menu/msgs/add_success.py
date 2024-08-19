import sys

def add_success():
    sys.path.append('C:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/view')
    from v_global_functions.clear_terminal import clean_terminal

    clean_terminal()
    print("Data registred with success!\n")
    input("Press enter to continue...")
    clean_terminal()