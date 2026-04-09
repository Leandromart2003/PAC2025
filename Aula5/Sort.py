# ===============================
# CONTROLO DE FLUXOS – EXEMPLOS
# ===============================

# -------------------------------
# Exemplo 1: Código ASCII
# -------------------------------
# Imprime os primeiros 255 caracteres ASCII

for i in range(1, 256):
    print(f"{i} -> {chr(i)}")

print(f"Código ASCII da letra 'o': {ord('o')}")


# -------------------------------
# Exemplo 2: Ordenação (Bubble Sort)
# -------------------------------

numeros = [3, 2, 7, 9, 4, 6, 1]

print("\nLista original:", numeros)
print("Tamanho da lista:", len(numeros))

# Algoritmo Bubble Sort
houve_troca = True

while houve_troca:
    houve_troca = False
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i + 1]:
            # troca de elementos
            numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
            houve_troca = True

print("Lista ordenada:", numeros)


# -------------------------------
# Exemplo 3: Manipulação de Strings em Lista
# -------------------------------

nomes = ["Joana Quental", "Joao Quental", "Pedro Lameiro"]

# Aceder a um carácter específico
print("\nLetra na posição 6 do primeiro nome:", nomes[0][6])

# Comparar caracteres
if nomes[0][6] == nomes[1][6]:
    print("Os caracteres são iguais")
else:
    print("Os caracteres são diferentes")

# trocar elemento da lista
nomes[0],nomes[1] = nomes[1],nomes[0]

print("Lista atualizada:", nomes)