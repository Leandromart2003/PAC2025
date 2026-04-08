#multiplas dimençoes

lista=["dario","Joao"]

for i in range(len(lista)):
    print("i na 1 dimençao nome completo : ", i , "nome : ", lista[i])
    for it in range(len(lista[i])):
        print("it na 2 dimençao :",it ,"letra correspondente", lista[i][it])

