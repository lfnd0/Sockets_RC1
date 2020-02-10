import socket
import sys

HOST = "localhost"
HOST_PORTA = 5001
TAMANHO_BUFFER = 4096

nome_arquivo = sys.argv[1]

print(f"[*] Conectando cliente {HOST}:{HOST_PORTA}")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"[*] Cliente conectado.")

s.sendto(nome_arquivo.encode(), (HOST, HOST_PORTA))
print(f"[+] Enviando o arquivo: {nome_arquivo}")

a = open(nome_arquivo, "rb")
arquivo = a.read(TAMANHO_BUFFER)

while(arquivo):
    if(s.sendto(arquivo, (HOST, HOST_PORTA))):
        arquivo = a.read(TAMANHO_BUFFER)

print(f"[+] Arquivo {nome_arquivo} enviado!")

s.close()
a.close()