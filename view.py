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
                    verifica = registar_jogador(jogadores, nome)
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
                    if n == players:
                         print('\tAVISO: O tabuleiro tem de ter entre 5-15 linhas e 5-15 colunas\n')
                         linhas = int(input('Digite o numero de linhas que deseja que o seu tabuleiro tenha:\n-->'))
                         colunas = int(input('Digite o numero de colunas que quer que o seu tabuleiro tenha:\n-->'))
                         if linhas >=5 and colunas >= 5 and linhas <= 15 and colunas <=15 :
                             tabuleiro = criar_tabuleiro_listas (linhas, colunas)

                             colunas_numeros ="  "+ "".join(f"{i+1:>2}" for i in range(colunas))
                             print(colunas_numeros)

                             for idx, linha in enumerate(tabuleiro):
                                print(f"{idx + 1:<3}" + " ".join(linha))  # Número da linha alinhado à esquerda

                              #------------COMECAR O JOGO EM SI --------
                             print ('Para jogar comece por indicar a linha e de seguida as colunas')
                             
                             ln = int(input('Indique o numero da linha\n-->'))
                             cl = int(input('Indique o numero da coluna\n-->')) 

                             ln = ln-1
                             cl = cl-1
                             if 0 <= ln < linhas and 0 <= cl < colunas:
                                  tabuleiro[ln][cl] = 'A'
                                  print('Tabuleiro atualizado:')
                                  devolver_tabuleiro(colunas, tabuleiro)

                         else:
                              print ('ERRO: Tamanho de tabuleiro inválido')

                    #------------------------------------------------------------------------------------ 

            case 3:
                  #---------Pontuações-------
               for j in jogadores:
                    print(f"Jogador: {j["Nome"]}, pontuação: {j["Pontuação"]}")

            case 4:
                  #---------Sair----------
                print ('Bye Bye, volte sempre Kiss Kiss :)')
                break
