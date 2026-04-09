# ===============================
# LISTAS E MÚLTIPLAS DIMENSÕES
# ===============================

lista=["dario",
       "Joao" ]

# Percorrer lista cada nome (1ª dimensão)
for i in range(len(lista)):
    print("i na 1 dimençao nome completo : ", i , "nome : ", lista[i])
    
    # Percorrer cada carácter do nome (2ª dimensão)
    for it in range(len(lista[i])):
        print("it na 2 dimençao :",it ,"letra correspondente", lista[i][it])

