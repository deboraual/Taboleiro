from controller import *

def main():
    jogadores = []
    while True:

        #------Menu-----
        operacao = int(input('\t\tMenu\n Escolha uma das seguintes operações:\n[1] - Registar Jogadores \n[2] - Jogar \n[3] - Pontuações \n[4] - Sair\nQual a sua opção: '))

        match operacao:
            case 1:
                  #---------Registar Jogador-------------------
                    nome = input ('Nome do jogador:\n-->')
                    cor = input('Escolha a cor da sua peça:\n-->')
                    verifica = registar_jogador(jogadores, nome, cor)
                    if verifica == False:
                         print('Nome de jogador ja existente')
                    else:
                         print('Jogador registado com sucesso\n')
                         print(jogadores)
            case 2:
                  #--------Verificar o número de jogadores antes de jogar-------- 
                 players = int(input('Quantos jogadores vão jogar, escolha entre 2 a 4\n-->'))

                 n = 0   
                 while n < players:
                    nome = input("Qual o nome do jogador: ")
                    verificar_nome = verificar_jogador(jogadores,nome)
                    if verificar_nome == False:
                         print("O utilizador não existe!") 
                         break    

                    n+=1

                    #------------------------------------------------------------------------------------ 

            case 3:
                  #---------Pontuações-------
               for j in jogadores:
                    print(f"Jogador: {j["Nome"]}, pontuação: {j["Pontuação"]}, cor: {j["Cor"]}")

            case 4:
                  #---------Sair----------
                print ('Bye Bye, volte sempre Kiss Kiss :)')
                break
