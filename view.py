from controller import *
from colorama import  Back, Style

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
                 if players < 2 or players > 4:
                      print('O minimo de jogadores são 2 e o maximo são 4.')
                      exit()
                 
                 jogadores_atuais = []
                 cores_jogadores =  [Back.BLUE, Back.RED, Back.YELLOW, Back.GREEN] #defenir as cores que vao ser utilizadas

                 n = 0   
                 while n < players:
                    nome = input("Qual o nome do jogador: ")
                    verificar_nome = verificar_jogador(jogadores,nome)
                    if verificar_nome == False:
                         print("O utilizador não existe!") 
                         break 
                    else:
                        jogadores_atuais.append({"nome": nome, "pecas": 21})   # vai adicionar os nomes ao dicionario jogadores atuais e das peças iniciais 

                    n+=1
                    if n == players:
                      print('\tAVISO: O tabuleiro tem de ter entre 5-30 linhas e 5-302 colunas\n')
                      linhas = int(input('Digite o numero de linhas que deseja que o seu tabuleiro tenha:\n-->'))
                      colunas = int(input('Digite o numero de colunas que quer que o seu tabuleiro tenha:\n-->'))

                      #definir os limites do tabuleiro nao pode ser menor que 5 por 5 nem maior que 15 por 15   
                      if linhas < 5 or linhas > 30 or colunas < 5 or colunas > 30:
                           print('Erro, tamanho de tabuleiro invalido!!')
                           break
                      

                      tabuleiro = criar_tabuleiro_listas(linhas, colunas)
          
                      #--------Taboleiro inicial--------
                      print('Tabuleiro inicial:')
                      devolver_tabuleiro(colunas, tabuleiro)
                      
                       #-----------Primeira jogada (1,1)----------
                      print(f'A primeira jogada tem de ser na posição (1,1) que calha a vez do/a jogador/a {jogadores_atuais[0]}')
                      tabuleiro[0][0] = '1'

                      for jogador in jogadores:
                          if jogador ["Nome"] == jogadores_atuais[0]["nome"]:
                              jogador["Pontuação"]+= 1
                              break

                      historico_jogadas = [[]for _ in range(players)] #lista de listas para armazenar todas as jogadas de cada jogador
                      historico_jogadas[0].append((0,0))
                      tabuleiro_colorido(colunas, tabuleiro, cores_jogadores)
                      jogador_atual = 0 

                      jogadores_atuais[jogador_atual]["pecas"] -= 1
                      
                      #-----------Jogar----------
                      total_jogadas = linhas * colunas - 1
                      jogadas_realizadas = 0
                      jogador_atual = 1

                      while jogadas_realizadas < total_jogadas:
                          #verificar se ainda tem jogadas validas 
                          if not jogadas_validas(tabuleiro, historico_jogadas,jogador_atual,linhas,colunas):
                              print(f"Jogador {jogadores_atuais[jogador_atual]['nome']} não pode mais jogar e será eliminado.")
                              if players == 2:
                                vencedores, pontuacao = deterinar_vencedor(jogadores)
                                print(f"O jogador {vencedores} ganhou e com {pontuacao} pontos")
                              jogador_atual = (jogador_atual + 1) % players
                              break
                          


                          print(f'É a vez do jogador {jogadores_atuais[jogador_atual]["nome"]}, Peças: {jogadores_atuais[jogador_atual]["pecas"]}')
                          ln_input = int(input('Digite o número da linha:\n-->'))
                          cl_input = int(input('Digite o número da coluna:\n-->'))

                          
                          ln = ln_input - 1
                          cl = cl_input - 1
                          
                          #verificar se a posição esta dentro dos limites do tabuleiro
                          if ln < 0 or ln >= linhas or cl < 0 or cl >= colunas:
                              print('Posicao fora dos limites do tabuleiro')
                              continue 
                          
                          #verifica se a posicao nao tem X, caso nao tenha a posicao eesta ocupada
                          if tabuleiro [ln][cl] != 'X':
                              print('Posição ocupada')
                              continue 
                           
                          #ver adjacencia tendo em conta as jogadas anteriores feitas
                          if not verificar_movimentos(tabuleiro, ln, cl, historico_jogadas,jogador_atual):
                              print('Posição invalida, nao adjacente a nenhuma jogada anterior')
                              continue
                          
                          #Atualizar o tabuleiro com a jogada atual
                          tabuleiro[ln][cl] = str(jogador_atual + 1)
                          print('Tabuleiro atualizado: ')
                          tabuleiro_colorido(colunas, tabuleiro, cores_jogadores)


                          #pontuacao
                          for jogador in jogadores:
                              if jogador["Nome"] == jogadores_atuais[jogador_atual]["nome"]:
                                  jogador["Pontuação"] += 1
                                  break
                              
                          # Adicionar a jogada ao historico do jogador            
                          historico_jogadas[jogador_atual].append((ln,cl))

                          jogadores_atuais[jogador_atual]["pecas"] -= 1

                          jogadas_realizadas += 1
                          jogador_atual = (jogador_atual + 1) % players



                          if jogadores_atuais[jogador_atual]["pecas"] <= 0:
                              print(f"O jogador {jogadores_atuais[jogador_atual]['nome']} ficou sem peças.")

                          jogadores_restantes = [j for j in jogadores_atuais if j["pecas"]>0]
                          if len(jogadores_restantes) <= 1:
                              print ('nenhum jogador pode jogar mais, o jogo acabou')
                              vencedores, pontuacao = deterinar_vencedor(jogadores)
                              if len(vencedores) == 1:
                                  print(f"O vecedor é {vencedores[0]} com {pontuacao} pontos!")
                                  
                              else:
                                  print(f"Empate, od vencedores sao {', '.join(vencedores)}com {pontuacao} pontos ")
                                  


                              



                    #------------------------------------------------------------------------------------ 

            case 3:
                  #---------Pontuações-------
               for j in jogadores:
                    print(f"Jogador: {j["Nome"]}, pontuação: {j["Pontuação"]}")

            case 4:
                  #---------Sair----------
                print ('Bye Bye, volte sempre Kiss Kiss :)')
                break