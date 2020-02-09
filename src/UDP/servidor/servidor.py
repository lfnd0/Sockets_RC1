import socket
import select
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORTA = 5001
BUFFER_TAMANHO = 4096
TIME_OUT = 2

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((SERVER_HOST, SERVER_PORTA))

while True:
    print(f"[*] Servidor UDP ativo em: {SERVER_HOST}:{SERVER_PORTA}")
    
    arquivo, endereco = socket.recvfrom(BUFFER_TAMANHO)
    if arquivo:
        nome_arquivo = os.path.basename(arquivo)
        print(f"[+] Recebendo arquivo: {nome_arquivo}")
    
    a = open(arquivo, "wb")

    while True:
        leitura = select.select([socket], [], [], TIME_OUT)
        if leitura[0]:
            arquivo, endereco = socket.recvfrom(BUFFER_TAMANHO)
            a.write(arquivo)
        else:
            print(f"[+] Arquivo recebido: {nome_arquivo}!")
            a.close()
            break