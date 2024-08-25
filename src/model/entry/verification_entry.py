
def v_entry(data_v_entry):

    def verification_plate(data_v_entry):

        plate = plate[0]

        if len(plate) == 7:   
            for i, item in enumerate(plate):

                if item.isalpha() and (i == 0 or i == 1 or i == 2 or i ==4):
                    contLetter += 1

                elif item.isdigit() and (i == 3 or i == 4 or i == 5 or i == 6):                      
                    contNum += 1
                        
            if (contLetter == 3 and contNum == 4) or (contLetter == 4 and contNum == 3):    
                plate_true = 1
                    
                if plate_true == 1:  

                    return True
                
        return False
    
    verification_plate(data_v_entry)