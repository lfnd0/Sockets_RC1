import socket
import os

SERVER_HOST = "0.0.0.0"
PORTA_SERVER = 5001
TAMANHO_BUFFER = 4096
MASCARA = "<MASCARA>"

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[*] Ativando servidor {SERVER_HOST}:{PORTA_SERVER}")

socket.bind((SERVER_HOST, PORTA_SERVER))
socket.listen(4)
print(f"[*] Servidor ativo.")

socket_cliente, endereco = socket.accept()
print(f"[+] Cliente {endereco} conectado.")

resposta = socket_cliente.recv(TAMANHO_BUFFER).decode()

nome_arquivo, tamanho_arquivo =  resposta.split(MASCARA)

nome_arquivo = os.path.basename(nome_arquivo)
tamanho_arquivo = int(tamanho_arquivo)

pegar_tamanho_arquivo = range(tamanho_arquivo)
with open(nome_arquivo, "wb") as a:
    for t in pegar_tamanho_arquivo:
        leitura_bytes = socket_cliente.recv(TAMANHO_BUFFER)
        if not leitura_bytes:
            break
        a.write(leitura_bytes)

socket_cliente.close()
socket.close()
print(f"[+] Arquivo {nome_arquivo} recebido!")