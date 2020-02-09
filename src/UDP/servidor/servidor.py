import socket
import select
import os

SERVER_HOST = "0.0.0.0"
PORTA_SERVER = 5001
TAMANHO_BUFFER = 4096
TIME_OUT = 2

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((SERVER_HOST, PORTA_SERVER))

while True:
    print(f"[*] Servidor UDP ativo em: {SERVER_HOST}:{PORTA_SERVER}")
    
    arquivo, endereco = socket.recvfrom(TAMANHO_BUFFER)
    if arquivo:
        nome_arquivo = os.path.basename(arquivo)
        print(f"[+] Recebendo arquivo: {nome_arquivo}")
    
    a = open(arquivo, "wb")

    while True:
        leitura = select.select([socket], [], [], TIME_OUT)
        if leitura[0]:
            arquivo, endereco = socket.recvfrom(TAMANHO_BUFFER)
            a.write(arquivo)
        else:
            print(f"[+] Arquivo recebido: {nome_arquivo}!")
            a.close()
            break