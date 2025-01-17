from colorama import Back, Style

def verificar_jogador(matriz,nome):
    
    for j in matriz:
          if nome == j["Nome"]:
               return True
    return False        
   
   
def registar_jogador(matriz,nome):
    if verificar_jogador(matriz,nome) == True:
          return False
    else:     
     j = {"Nome": nome.lower(), "Pontuação": 0}
     matriz.append(j)
     return True
    

#-----Função professora tabuleiro com listas 

def criar_tabuleiro_listas(linhas, colunas):
    tabuleiro = []
    for i in range(linhas): 
        linha = []
        for j in range(colunas):  
            linha.append("X")  
        tabuleiro.append(linha)  
    return tabuleiro

#------Função para devolver o tabuleiro com a linha e coluna do utilizador 
def devolver_tabuleiro ( colunas, tabuleiro):

     colunas_numeros ="  " + "".join(f"{i+1:>2}" for i in range(colunas))
     print(colunas_numeros)

     for idx, linha in enumerate(tabuleiro):
         print(f"{idx + 1:<3}" + " ".join(linha))

def tabuleiro_colorido (colunas, tabuleiro, cores_jogadores):
     
     colunas_numeros = "  " + "".join(f"{i + 1:>2}" for i in range(colunas))
     print(colunas_numeros)

     for idx, linha in enumerate(tabuleiro):
         linha_formatada = []
         for cell in linha:
            if cell != "X":
                jogador_index = int(cell)-1
                cor = cores_jogadores[jogador_index]
                linha_formatada.append(cor + cell + Style.RESET_ALL)

            else:
                linha_formatada.append(cell)
         print(f"{idx + 1:<3}" + " ".join(linha_formatada))
                 

def verificar_movimentos(tabuleiro, linha, coluna, historico_jogadas, jogador_atual):
    if not historico_jogadas[jogador_atual]:
        return True 
    
    movimentos = {
        (-1,0), #cima
        (1,0), #baixo
        (0,-1),#esquerda 
        (0,1),#direita
        (-1,-1),#up esq
        (-1,1),#up drt
        (1,-1),#inf esq
        (1,1) #inf drt
    }

    for jogada_ant in historico_jogadas[jogador_atual]:
        ultima_linha, ultima_coluna = jogada_ant
        for mov in movimentos:
            nova_linha = ultima_linha + mov[0]
            nova_coluna = ultima_coluna + mov [1]
            if nova_linha == linha and nova_coluna == coluna:
                return True 
    return False 

def jogadas_validas (tabuleiro, historico_jogadas, jogador_atual, linhas, colunas):
    for ln in range(linhas):
        for cl in range(colunas):
            if tabuleiro [ln][cl]=='X'and verificar_movimentos(tabuleiro, ln,cl, historico_jogadas, jogador_atual):
                return True
    return False


#-------- Função dicionar bonus - Verifica se a posição atual corresponde a uma posição de bônus-------
coordenadas_bonus = [(5, 3), (18, 25), (22, 7), (9, 30), (15, 15), (3, 20), (27, 4), (11, 11), (6, 28), (29, 3)]


def verificar_bonus (linha, coluna, jogadores):
    if (linha + 1, coluna + 1) in coordenadas_bonus: #adiciona 1 porque o jogador usa indices baseados em 1
        print (f"Parabéns! Jogador {jogadores['Nome']} ganhou 2 pontos ao jogo em uma posicao de bonus!")
        jogadores ['Pontuação'] += 2

        return True
    
    else: 
        return False


def deterinar_vencedor(jogadores):
    maior_pontuacao = -1
    vencedor = []

    for jogador in jogadores:
        if jogador ["Pontuação"] > maior_pontuacao:
            maior_pontuacao = jogador["Pontuação"]
            vencedor = [jogador["Nome"]]
        elif jogador["Pontuação"] == maior_pontuacao:
            vencedor.append(jogador["Nome"])#empate

    return vencedor, maior_pontuacao









#cores para os jogadores: azul, vermelho, amarelo e verde