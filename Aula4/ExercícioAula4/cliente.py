import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
porta = 12340

clientSocket.connect((host, porta))
print("Ligado ao servidor! (Escreve 'sair' para terminar)")
try:
    while True:
        mensagem = input("Mensagem para o servidor: ")
        if not mensagem:
            continue
        clientSocket.send(mensagem.encode())
        if mensagem.lower() == "sair":
            break
        resposta = clientSocket.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")
finally:
    clientSocket.close()
    print("Conexão fechada.")