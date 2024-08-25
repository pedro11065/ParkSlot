import sys

def menu():
    
    sys.path.append('C:/Users/fsxre/OneDrive/GitHub/ParkSlot/src/view')
    from v_global_functions.clear_terminal import clean_terminal

    clean_terminal()

    print("What you would like to do?:\n")
    menu_job = input("Add new car(A)\nSearch a car(S)\nList all cars(L)\nDelete a car(D)\nSee historic(H)\n:")

    clean_terminal()

    match menu_job:
        case "A":
            return "0"
        case "S":
            return "1"
        case "L":
            return "2"
        case "D":
            return "3"
        case "H":
            return "4"
