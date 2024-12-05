from controller import *

def main():
    jogadores = []
    while True:

        #------Menu-----
        operacao = int(input('\t\tMenu\n Escolha uma das seguintes operações:\n1 --> Registar Jogadores \n2--> Jogar \n3-->Pontuações \n4 --> Sair\n-->'))

        match operacao:
            case 1:
                    nome = input ('Nome do jogador:\n-->')
                    verifica = registar_jogador(jogadores, nome)
                    if verifica == False:
                         print('Nome de jogador ja existente')
                    else:
                         print('Jogador registado com sucesso\n')
                         print(jogadores)
            case 2:
                  #--------JOGAR--------
                 players = int(input('Quantos jogadores vão jogar, escolha entre 2 a 4\n-->'))
                 if players == 2 or players == 3 or players == 4:
                      pass
                 else:
                      print('O que inseriu está incorreto')
            case 3:
                  pass
                         
            case 4:
                print ('Bye Bye, volte sempre Kiss Kiss :)')
                break
