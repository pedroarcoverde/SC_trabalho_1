#!/usr/bin/python3

import base64
import os

import RSA3
import AES


msg = open('texto.txt', 'r').read() 

while(op != 4):
    op = int(input("ESCOLHA UMA OPÇÃO:\n\n1) GERAR CHAVES\n2) CIFRAR\n3) DECIFRAR\n4) FECHAR\n"))

    # GERA AS CHAVES PÚBLICAS E PRIVADAS
    if op == 1:
        chave_publica, chave_privada = RSA3.gera_chaves()

    # CIFRA E ASSINA A MSG
    elif op == 2:
        chave = os.urandom(16)
        iv = os.urandom(16)

        chave_sess = chave + iv



    elif op == 3:
        continue

    elif op == 4:
        break

    else:
        continue

