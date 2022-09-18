#!/usr/bin/python3

import base64
import secrets

import RSA3
import AES



while(op != 4):
    op = int(input("ESCOLHA UMA OPÇÃO:\n\n1) GERAR CHAVES\n2) CIFRAR\n3) DECIFRAR\n4) FECHAR\n"))

    # GERA AS CHAVES PÚBLICAS E PRIVADAS
    if op == 1:
        chave_publica, chave_privada = RSA3.gera_chaves()

    # CIFRA E ASSINA A MSG
    elif op == 2:
        secrets.token_bytes(16), secrets.token_bytes(16)
        chave, iv = secrets.token_bytes(16), secrets.token_bytes(16)

        chave_sess = chave + iv
        chave_sess_cifra = RSA3.cifra(chave_publica, chave_sess)
        chave_sess_cifra = base64.b64encode(chave_sess_cifra).decode("ascii")

        msg = open('texto.txt', 'r').read() 
        msg_cifrada = AES.ctr(msg, chave, iv)

        assinatura = RSA3.assina(chave_privada, msg)
        assinatura = base64.b64encode(assinatura).decode("ascii")

    # DECIFRA E VERIFICA ASSINATURA DA CIFRA
    elif op == 3:
       
        assinatura = base64.b64decode(assinatura)





    # ENCERRA O PROGRAMA
    elif op == 4:
        break

    else:
        continue

