"""
objetivo: Criar um programa capaz de armazenar as placas dos carros quando eles chegarem,
contabilizar quanto o motorista dono daquela placa deve pagar quando sair 
levando em consideração o tempo que ele ficou no estacionamento.

 Até 1h = R$5; ademais, cada hora = R$3 (1 minuto a mais vale como 1h)

A "interface" do programa deve ser de fácil compreenção para leigos que irão usar o programa.(porteiro)

### valido somente para o mesmo dia!!! ###


"""
import sys
import os
car_id = []
car_list = []
hour_list = []

while True:

    def data():#entrada básica
        while True:
            tarefa = input("O que você deseja fazer?\n(e)ntrada\n(s)aida \n(l)istar\ndigite: ")
            
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

            return job, job_name

    def call(data_data):#faz os comandos funcionarem
        if data_data[0] == 1:
            entry(data_data)

        elif data_data[0] == 2:
            exit(data_data)

        elif data_data[0] == 3:  
            list(data_data)

    def entry(data_data): #entrada
        
        job = data_data[0]
        job_name = data_data[1]
        hour_true = 0

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\ncomando: {job_name}\n")
        
        if job == 1:
            
            car_in = input("Digite a placa do carro:\n")
            
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
                hour_true = 1
                
            if hour_true == 1:

                hour_in = int(input("\nQue horas são?(ex:1303 = 13h03):\n"))
                hour_list.append(hour_in)

                os.system('cls' if os.name == 'nt' else 'clear')
                print("Dados registrados.")
                hour_true == 0
                
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\ncomando: {job_name}\n")
                
                print("Placa invalida, por favor digite novamente.\n")
        else:
            print("Error entrada")
            #adicionar returns

    def exit(data_data): #saida
        
        job = data_data[0]
        job_name = data_data[1]
        
        if  job == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\ncomando: {job_name}\n")
            
            if car_list != []:
                #depois de criar as funções, chamar a lista
                list(data_data)
                
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
            
        else:
            print("Error exit")
        
        #adicionar returns

    def list(data_data): #listar
        
        job = data_data[0]
        job_name = data_data[1]
        
        if job == 3: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\ncomando: {job_name}\n")
            
            if car_list != []:
                i_num = 0
                hour = hour_list[i_num]
            
                print("ID   Placa   Chegada")
                for car in car_list:
                    print(f"{i_num}...{car.upper()}...{hour}")
                    i_num += 1
                print("\n")
            else:      
                print("Não há nenhum carro registrado no estacionamento para ser listado.\n")
        
        else:
            i_num = 0
            hour = hour_list[i_num]
            print("ID   Placa   Chegada")
            for car in car_list:
                print(f"{i_num}...{car.upper()}...{hour}")
                i_num += 1
            print("\n")

    data_data = data()

    #print(data_data[0])#1 = job
    #print(data_data[1])#entrada = job_name

    call(data_data)
