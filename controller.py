
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
    











#cores para os jogadores: azul, vermelho, amarelo e verde