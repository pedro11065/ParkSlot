"""
objetivo: Criar um programa capaz de armazenar as placas dos carros quando eles chegarem,
contabilizar quanto o motorista dono daquela placa deve pagar quando sair 
levando em consideração o tempo que ele ficou no estacionamento.

 Até 1h = R$5; ademais, cada hora = R$3 (1 minuto a mais vale como 1h)

A "interface" do programa deve ser de fácil compreenção para leigos que irão usar o programa.(porteiro)

### valido somente para o mesmo dia!!! ###

#####################################################################################
entrada
"""
import sys
import os

car_id = []
car_list = []
hour_list = []
while True:
    
    tarefa = input("""O que você deseja fazer?
    (e)ntrada
    (s)aida 
    (l)istar
                    
    digite: """)

###########################################################################################
#validação
    
    if tarefa == "e":
        job = 1
        job_name = "entrada"

    elif tarefa == "s":
        job = 2
        job_name = "saida"

    elif tarefa == "l":
        job = 3
        job_name = "listar"

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Digite um comando válido")
        continue
    
##############################################################################
#entrada
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"\ncomando:{job_name}\n")
    
    if job == 1: #entrada
        
        car_in = input("Digite a placa do carro:\n")
        car_in.upper()
        
        contLetra = 0
        contNum = 0
        #verificar placa
        if len(car_in) == 7:
            for i, item in enumerate(car_in):
                #verificar as letras, se existem e se estão nas posições certas
                if item.isalpha() and (i == 0 or i == 1 or i == 2 or i ==4):
                    contLetra += 1
                elif item.isdigit() and (i == 3 or i == 4 or i == 5 or i == 6):
                    contNum += 1
        if (contLetra == 3 and contNum == 4) or (contLetra == 4 and contNum == 3):      
              car_list.append(car_in)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\ncomando:{job_name}\n")
            
            print("Placa invalida, por favor digite novamente.\n")
            continue

        hour_in = int(input("\nQue horas são?(ex:1303 = 13h03):\n"))
        hour_list.append(hour_in)
        
        print("Dados registrados.")
        
    ##########################################################################################
    
    elif job == 2: #saida
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\ncomando:{job_name}\n")
        
        if car_list != []:
            #depois de criar as funções, chamar a lista
            out_car = input("Qual é a placa do carro?(minúsculo)")
            out_hour = int(input("Que horas são? (ex:1303 = 13h03):\n"))

            i_car = car_list.index(out_car) #indice dessa placa na lista
            i_hour = i_car
            
            value_simple = (out_hour - hour_list[i_hour]) / 100
            value5 = (value_simple - (value_simple - 1)) * 5
            value3 = (value_simple - 1) * 3
            value_final = value5 + value3

            print(f"""\nO carro da placa {car_list[i_car]} ficou o total de {value_simple} horas no estacionamento.\n
            O valor a ser pago é de:R${value_final:.2}\n""")

            del car_list[i_car]
            del hour_list[i_hour]
        else:
            print("Não há nenhum carro registrado no estacionamento.\n")
    ##########################################################################################

    elif job == 3: #listar
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\ncomando:{job_name}\n")
        
        if car_list != []:
            i_num = 0
            hour = hour_list[i_num]
        
            print("ID   Placa   Chegada")
            for car in car_list:
                print(f"{i_num}...{car}...{hour}")
                i_num += 1

        else:      
            print("Não há nenhum carro registrado no estacionamento para ser listado.\n")

