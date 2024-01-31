import os
import addAsk as add

rep = 2

while rep == 2:
    print("Gerenciador de Tarefas... \n")
    print("Escolha o que deseja realizar:\n")
    print("1 - Visualizar tarefas ")
    print("2 - Adicionar tarefas ")
    print("3 - Excluir tarefas")
    print("4 - Concluir tarefas\n")
    option = int(input("Opção -> "))
    match option: 
        case 1: 
            print("caso 1")
        case 2: 
            print("caso 2")
        case 3: 
            print("caso 3")
        case 4: 
            print("caso 4")
        case _: 
            print("Digite uma opção válida")
            
    os.system("cls")

    print("Deseja fechar o programa\n")
    print("1 - SIM\n2 - NÂO")
    rep = int(input("->"))
    
    os.system("cls")
    
