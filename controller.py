
def verificar_jogador(matriz,nome):
    
    for j in matriz:
          if nome == j[0]:
               return True
    return False        
   
   
def registar_jogador(matriz,nome):
    if verificar_jogador(matriz,nome) == True:
          return False
    else:     
     j = [nome, 0]
     matriz.append(j)
     return True
    
def ver_pontuacoes ():
    pass