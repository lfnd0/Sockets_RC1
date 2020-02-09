import socket
import sys
import os
import argparse

HOST = "localhost"
PORTA_HOST = 5001
TAMANHO_BUFFER = 4096
MASCARA = "<MASCARA>"

def enviar_arquivo(nome_arquivo):
    tamanho_arquivo = os.path.getsize(nome_arquivo)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[*] Conectando cliente {HOST}:{PORTA_HOST}")

    s.connect((HOST, PORTA_HOST))
    print(f"[*] Cliente conectado.")

    s.send(f"{nome_arquivo}{MASCARA}{tamanho_arquivo}".encode())
    print(f"[+] Enviando o arquivo: {nome_arquivo}")

    pegar_tamanho_arquivo = range(tamanho_arquivo)
    with open(nome_arquivo, "rb") as a:
        for t in pegar_tamanho_arquivo:
            leitura_bytes = a.read(TAMANHO_BUFFER)
            if not leitura_bytes:
                break
            s.sendall(leitura_bytes)
    s.close()
    print(f"[+] Arquivo {nome_arquivo} enviado!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("arquivo")
    args = parser.parse_args()
    nome_arquivo = args.arquivo
    enviar_arquivo(nome_arquivo)