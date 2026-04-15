import requests   # Biblioteca para pedidos HTTP
import time       # Para controlar intervalos entre pedidos

# URL base da API
BASE_URL = "https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx"

# Cabeçalhos HTTP (identificação do crawler)
HEADERS = {
    "User-Agent": "EducationalCrawler/1.0 (uso académico)"
}

# Função que vai buscar dados para um determinado ID
def obter_dados(user_id):
    
    # Parâmetros enviados no pedido
    params = {
        "command": "_SelectAllSchedulesDataSetGivenByUserId",
        "oId": user_id,  # ID a testar
        "idField": "DataValueField",
        "titleField": "DataTextField",
        "startDateField": "DataStartField",
        "endDateField": "DataEndField",
        "textColorField": "textcolor",
        "eventColorField": "color",
        "description": "description",
        "picField": "pic",
        "urlField": "url",
        "start": "1776034800",
        "end": "1776639600"
    }

    try:
        # Pedido GET à API
        resposta = requests.get(
            BASE_URL,
            params=params,
            headers=HEADERS,
            timeout=5
        )

        # Verifica se correu bem
        if resposta.status_code == 200:
            return resposta.json()  # devolve dados em JSON
        else:
            print(f"[ERRO] ID {user_id} → Status: {resposta.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Captura erros de ligação
        print(f"[EXCEÇÃO] ID {user_id} → {e}")
        return None

# Função principal do crawler
def crawler(inicio=7000, fim=7010, delay=1):
    resultados = []

    # Percorre intervalo de IDs
    for user_id in range(inicio, fim + 1):
        print(f"[INFO] A processar ID: {user_id}")

        dados = obter_dados(user_id)

        # Guarda apenas se houver dados
        if dados:
            resultados.append({
                "user_id": user_id,
                "dados": dados
            })

        # Pausa entre pedidos (boa prática)
        time.sleep(delay)

    return resultados

dados_recolhidos = crawler(7000, 7010, delay=1)

print("\nResumo:")
print(f"Total de registos: {len(dados_recolhidos)}")