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

def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao_email, email):
        return True
    else:
        return False
        
def extrair_dominio(email):
    padrao_dominio = r'@([\w\.-]+)$'
    resultado = re.search(padrao_dominio, email)
    if resultado:
        return resultado.group(1)
    else:
        return None
    

def validar_nifs(nif):
    padrao_nif = r'^[123568]\d{8}$'
    if re.match(padrao_nif, nif):
        return True
    else:
        return False
    

