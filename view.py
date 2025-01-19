from controller import *
from colorama import  Back

def main():
    jogadores = []
    while True:

        #------Menu-----
        operacao = int(input('\t\tMenu\n Escolha uma das seguintes operações:\n[1] - Registar Jogadores \n[2] - Jogar \n[3] - Pontuações \n[4] - Gravar Dados \n[5] - Ler Dados \n[6] - Sair \nQual a sua opção: '))

        match operacao:
            case 1:
                  #---------Registar Jogador-------------------
                    quantidade_registar = int(input("Quantos jogadores deseja registar: "))

                    x = 0
                    while x < quantidade_registar:
                        nome = input('Nome do jogador:\n-->')
                        
                        if not nome:  # Verifica se o nome está vazio
                            print("Nome não pode ser vazio. Tente novamente.")
                            continue  # Pede para o usuário tentar novamente

                        verifica = registar_jogador(jogadores, nome)
                        if verifica == False:
                            print('Nome de jogador já existente')
                        else:
                            print('Jogador registado com sucesso\n')
                            x += 1  # Corrigido: Incrementa x corretamente
            case 2:
                  #--------Verificar o número de jogadores antes de jogar--------
                  
                    players = int(input('Quantos jogadores vão jogar, escolha entre 2 a 4\n-->'))
                    if players < 2 or players > 4:
                        print('O mínimo de jogadores são 2 e o máximo são 4.')
                        exit()

                    jogadores_atuais = []
                    cores_jogadores = [Back.BLUE, Back.RED, Back.YELLOW, Back.GREEN]  # Definir as cores que vão ser utilizadas

                    n = 0
                    jogadores_atuais = []  # Lista para armazenar os jogadores registrados

                    while n < players:
                        nome = input("Qual o nome do jogador: ")
                        verificar_nome = verificar_jogador(jogadores, nome)
                        
                        if verificar_nome == False:
                            print("O utilizador não existe!") 
                        else:
                            jogadores_atuais.append({"nome": nome, "pecas": 21})  # Adiciona o jogador com 21 peças iniciais
                            n += 1

                    # Perguntar o modo de jogo após registrar todos os jogadores
                    if players == 4:
                        modo = input("Qual o modo que deseja jogar ('solo/duo'): ").lower()

                        if modo == "duo":
                            print("Criando as equipas......")
                            equipa_1 = [jogadores_atuais[0], jogadores_atuais[1]]  # Corrigido a estrutura
                            equipa_2 = [jogadores_atuais[2], jogadores_atuais[3]]

                            print("Modo de jogo: Duo")
                            print(f"Equipa 1: {equipa_1}")
                            print(f"Equipa 2: {equipa_2}")

                        elif modo == "solo":
                            # Todos jogam individualmente
                            print("Modo de jogo: Solo")
                            for i, jogador in enumerate(jogadores_atuais):
                                print(f"Jogador {i + 1}: {jogador}")

                        else:
                            print("Modo inválido. Escolha entre 'solo' ou 'duo'.")

                    if n == players:
                        print('\tAVISO: O tabuleiro tem de ter entre 5-30 linhas e 5-30 colunas\n')
                        linhas = int(input('Digite o número de linhas que deseja que o seu tabuleiro tenha:\n-->'))
                        colunas = int(input('Digite o número de colunas que quer que o seu tabuleiro tenha:\n-->'))

                        # Definir os limites do tabuleiro não pode ser menor que 5 por 5 nem maior que 15 por 15   
                        if linhas < 5 or linhas > 30 or colunas < 5 or colunas > 30:
                            print('Erro, tamanho de tabuleiro inválido!!')
                            exit()

                        tabuleiro = criar_tabuleiro_listas(linhas, colunas)
                        
                        #--------Tabuleiro inicial--------
                        print('Tabuleiro inicial:')
                        devolver_tabuleiro(colunas, tabuleiro)
                        
                        #-----------Primeira jogada (1,1)----------
                        print(f'A primeira jogada tem de ser na posição (1,1) que calha a vez do/a jogador/a {jogadores_atuais[0]}')
                        tabuleiro[0][0] = '1'

                        for jogador in jogadores:
                            if jogador["Nome"] == jogadores_atuais[0]["nome"]:
                                jogador["Pontuação"] += 1
                                break

                        historico_jogadas = [[] for _ in range(players)]  # Lista de listas para armazenar todas as jogadas de cada jogador
                        historico_jogadas[0].append((0, 0))
                        tabuleiro_colorido(colunas, tabuleiro, cores_jogadores)
                        jogador_atual = 0

                        jogadores_atuais[jogador_atual]["pecas"] -= 1
                        
                        #-----------Jogar----------
                        total_jogadas = linhas * colunas - 1
                        jogadas_realizadas = 0
                        jogador_atual = 1

                        while jogadas_realizadas < total_jogadas:

                            # Verificar se ainda tem jogadas válidas
                            if not jogadas_validas(tabuleiro, historico_jogadas, jogador_atual, linhas, colunas):
                                print(f"Jogador {jogadores_atuais[jogador_atual]['nome']} não pode mais jogar e será eliminado.")
                                jj = jogadores_atuais[jogador_atual]
                                jogadores_atuais.remove(jj)#remove o jogador atual dos jogadores 

                                if players == 2:
                                    #O jogador que ganhou ira ganhar mais 5 pontos por ter ganho 
                                    for jogador in jogadores:
                                     if jogador["Nome"] == jogadores_atuais[jogador_atual]["nome"]:
                                      jogador["Pontuação"] += 5
                                      break
                                    
                                    vencedores, pontuacao = determinar_vencedor(jogadores)
                                    print(f"O jogador {jogadores_atuais[jogador_atual]['nome']} ganhou, com {pontuacao} pontos")
                                    break

                                # Passar para o próximo jogador
                                jogador_atual = (jogador_atual + 1) % players
                                continue  # passar para o próximo jogador, sem acabar o jogo

                            print(f'É a vez do jogador {jogadores_atuais[jogador_atual]["nome"]}, Peças: {jogadores_atuais[jogador_atual]["pecas"]}')
                            ln_input = int(input('Digite o número da linha:\n-->'))
                            cl_input = int(input('Digite o número da coluna:\n-->'))

                            ln = ln_input - 1
                            cl = cl_input - 1

                            # Verifica se a jogada está nas coordenadas que dão bônus
                            if (ln + 1, cl + 1) in coordenadas_bonus:
                                for jogador in jogadores:
                                    if jogador["Nome"] == jogadores_atuais[jogador_atual]["nome"]:
                                        jogador["Pontuação"] += 2
                                        print(f'Parabéns {jogadores_atuais[jogador_atual]["nome"]}! Recebeu 2 pontos extras!')
                                        break

                            # Verifica se a posição está dentro dos limites do tabuleiro
                            if ln < 0 or ln >= linhas or cl < 0 or cl >= colunas:
                                print('Posição fora dos limites do tabuleiro')
                                continue 

                            # Verifica se a posição está ocupada
                            if tabuleiro[ln][cl] != 'X':
                                print('Posição ocupada')
                                continue

                            # Verifica a adjacência das jogadas anteriores
                            if not verificar_movimentos(tabuleiro, ln, cl, historico_jogadas, jogador_atual):
                                print('Posição inválida, não adjacente a nenhuma jogada anterior')
                                continue

                            # Atualiza o tabuleiro com a jogada atual
                            tabuleiro[ln][cl] = str(jogador_atual + 1)
                            print('Tabuleiro atualizado: ')
                            tabuleiro_colorido(colunas, tabuleiro, cores_jogadores)

                            # Pontuação
                            for jogador in jogadores:
                                if jogador["Nome"] == jogadores_atuais[jogador_atual]["nome"]:
                                    jogador["Pontuação"] += 1
                                    break

                            # Adiciona a jogada ao histórico do jogador
                            historico_jogadas[jogador_atual].append((ln, cl))

                            # Atualiza as peças do jogador
                            jogadores_atuais[jogador_atual]["pecas"] -= 1

                            jogadas_realizadas += 1

                            # Passa para o próximo jogador
                            jogador_atual = (jogador_atual + 1) % players

                            # Verifica se o jogador atual ficou sem peças
                            if jogadores_atuais[jogador_atual]["pecas"] <= 0:
                                print(f"O jogador {jogadores_atuais[jogador_atual]['nome']} ficou sem peças.")
                            
                            # Verifica se ainda existem jogadores com peças
                            jogadores_restantes = [j for j in jogadores_atuais if j["pecas"] > 0]
                            
                            # Se não houver jogadores restantes, o jogo acaba
                            if len(jogadores_restantes) <= 1:
                                print('Nenhum jogador pode jogar mais, o jogo acabou.')
                                # Chama a função para determinar o vencedor
                                vencedores, pontuacao = determinar_vencedor(jogadores)
                                if len(vencedores) == 1:
                                    print(f"O vencedor é {vencedores[0]} com {pontuacao} pontos!")
                                else:
                                    print(f"Empate, os vencedores são {', '.join(vencedores)} com {pontuacao} pontos.")
                                break  # Encerra o jogo
                                                        

                    #------------------------------------------------------------------------------------ 

            case 3:
                  #---------Pontuações-------
               for j in jogadores:
                    print(f"Jogador: {j["Nome"]}, pontuação: {j["Pontuação"]}")

            case 4:
                escrever_ficheiro_json("jogadores.json", jogadores)
                print("Pontuações salvas com sucesso.")

            case 5:
                jogadores = ler_ficheiro_json("jogadores.json")
                print("Dados carregados:")
                print(jogadores)

            case 6:
                #---------Sair----------
                print('Bye Bye, volte sempre Kiss Kiss :)')
                break