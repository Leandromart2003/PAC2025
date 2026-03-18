import json
import re

def ler_json():
    try:
        with open ('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return dados
    except FileNotFoundError:
        print("Erro o ficheiro 'dados.json' não foi encontrado.")
        return []

lista_pessoas = ler_json()
print("dados carregados com sucesso!")
for pessoa in lista_pessoas:
    print(f"Nome: {pessoa['nome']}, Email: {pessoa['email']} ")

