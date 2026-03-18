import socket
import time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
host = "127.0.0.1"
porta = 12340
serverSocket.bind((host, porta))
serverSocket.listen(1)
print(f"Servidor ativo em {host}:{porta}")
clientSocket, endereco = serverSocket.accept()
print(f"Conectado a: {endereco}")
try:
    while True:
        data = clientSocket.recv(1024)
        time.sleep(1)  
        if not data:
            break
        mensagem = data.decode()
        print(f"Cliente disse: {mensagem}")
        resposta = f"Servidor recebeu: {mensagem}"
        clientSocket.send(resposta.encode())
        if mensagem.lower() == "sair":
            break
finally:
    clientSocket.close()
    serverSocket.close()
    print("Conexões encerradas.")