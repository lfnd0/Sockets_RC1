import socket
import os

SERVER_HOST = "0.0.0.0"
PORTA_SERVER = 5001
TAMANHO_BUFFER = 4096
MASCARA = "<MASCARA>"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[*] Servidor ativo em: {SERVER_HOST}:{PORTA_SERVER}")

s.bind((SERVER_HOST, PORTA_SERVER))
s.listen(4)
print(f"[*] Servidor ativo.")

s_cliente, endereco = s.accept()
print(f"[+] Cliente {endereco} conectado.")

resposta = s_cliente.recv(TAMANHO_BUFFER).decode()

nome_arquivo, tamanho_arquivo =  resposta.split(MASCARA)

nome_arquivo = os.path.basename(nome_arquivo)
tamanho_arquivo = int(tamanho_arquivo)

pegar_tamanho_arquivo = range(tamanho_arquivo)
with open(nome_arquivo, "wb") as a:
    for t in pegar_tamanho_arquivo:
        leitura_bytes = s_cliente.recv(TAMANHO_BUFFER)
        if not leitura_bytes:
            break
        a.write(leitura_bytes)

s_cliente.close()
s.close()
print(f"[+] Arquivo {nome_arquivo} recebido!")