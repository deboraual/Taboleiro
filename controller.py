
def verificar_jogador(matriz,nome):
    
    for j in matriz:
          if nome == j["Nome"]:
               return True
    return False        
   
   
def registar_jogador(matriz,nome,cor):
    if verificar_jogador(matriz,nome) == True:
          return False
    else:     
     j = {"Nome": nome, "Pontuação": 0, "Cor": cor}
     matriz.append(j)
     return True
    
def ver_pontuacoes ():
    pass