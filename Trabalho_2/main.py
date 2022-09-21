#!/usr/bin/python3

import base64
import secrets
from pathlib import Path

import RSA
import AES


op = 0
while(op != 4):
    op = int(input("ESCOLHA UMA OPÇÃO:\n\n1) GERAR CHAVES\n2) CIFRAR\n3) DECIFRAR\n4) FECHAR\n"))

    # GERA AS CHAVES PÚBLICAS E PRIVADAS
    if op == 1:
        chave_publica, chave_privada = RSA.gera_chaves()

        n, e = chave_publica
        n, d = chave_privada

        print(f'CHAVE PÚBLICA:\nN: {n}\nE: {e}\n')
        print(f'CHAVE PRIVADA:\nN: {n}\nD: {d}\n')
        input()

    # CIFRA E ASSINA A MSG
    elif op == 2:
        chave, iv = secrets.token_bytes(16), secrets.token_bytes(16)

        chave_sess = chave + iv
        chave_sess_cifra = RSA.cifra(chave_publica, chave_sess)
        chave_sess_cifra = base64.b64encode(chave_sess_cifra).decode("ascii")

        arq = input('\nNOME DO ARQUIVO A SER CIFRADO: ')
        print()
        arquivo = Path(__file__).absolute().parent / arq
        with open(arquivo, "rb") as f:
            msg = f.read()

        msg_cifrada = AES.ctr(msg, chave, iv)
        with open(arquivo, "wb") as f:
            f.write(msg_cifrada)

        assinatura = RSA.assina(chave_privada, msg)
        assinatura = base64.b64encode(assinatura).decode("ascii")

        print('MENSAGEM:\n')
        print(msg)
        input()
        print('\nMENSAGEM CIFRADA:\n')
        print(msg_cifrada)
        input()
        print('\nCHAVE DA SESSÃO:\n')
        print(chave_sess)
        print()
        input()
        print('\nCHAVE DA SESSÃO CIFRADA:\n')
        print(chave_sess_cifra)
        print()
        input()
        print('\nASSINATURA:\n')
        print(assinatura)
        print()
        input()

    # DECIFRA E VERIFICA ASSINATURA DA CIFRA
    elif op == 3:

        arq = input('\nNOME DO ARQUIVO A SER DECIFRADO: ')
        print()
        arquivo = Path(__file__).absolute().parent / arq
        with open(arquivo, "rb") as f:
            msg_cifrada = f.read()
       
        assinatura = base64.b64decode(assinatura)
        chave_sess_cifra = base64.b64decode(chave_sess_cifra)
        
        chave_sess = RSA.decifra(chave_privada, chave_sess_cifra)
        chave, iv = chave_sess[:16], chave_sess[16:]

        msg = AES.ctr(msg_cifrada, chave, iv)
        confere = RSA.verifica_assinatura(chave_publica, msg, assinatura)

        if confere:
            print("\nAssinatura confere\n")
            print('MENSAGEM:\n')
            print(msg)
            arquivo = Path(__file__).absolute().parent / arq
            with open(arquivo, "wb") as f:
                f.write(msg)
        else:
            print("\nAssinatura NÃO confere\n")



    # ENCERRA O PROGRAMA
    elif op == 4:
        break

    else:
        continue



# TEXTO PARA TESTES

# Lorem ipsum dolor sit amet. Qui voluptatem ipsa qui debitis distinctio veniam deleniti et molestiae blanditiis. Et ipsum voluptatem eum quis odio 33 fugit accusamus non quia perferendis aut facilis dolorum aut rerum quasi. Quo rerum fugit et libero voluptatum non unde voluptatem est dolorum eaque qui voluptatem aliquid ut autem voluptas. Aut aspernatur recusandae aut blanditiis impedit eum ipsum blanditiis et provident nulla quo debitis autem est voluptates odio quo exercitationem nostrum.

# Ex nesciunt dicta sit consequatur eius ea magnam soluta. Quo facere optio qui facilis illum et deserunt molestiae et molestias totam et sapiente aspernatur ea numquam quod et corporis asperiores. Sed tempore deserunt id esse minima non numquam dolores ut voluptate nobis qui quisquam iste eos quia possimus sit voluptatibus rerum. Non ipsam consectetur ex vitae dolor a aspernatur sunt sed explicabo perferendis.

# Sit minus assumenda ea reprehenderit omnis aut aperiam molestiae ad sint fugiat quo nesciunt ducimus. Ut voluptatem doloribus et rerum facere et dolore ut voluptatem modi aspernatur esse. Ea repellat magni hic explicabo ipsa et possimus officia a impedit quos qui suscipit laborum est voluptatem consequatur qui quas laborum. Ut modi dolores non error magni et reiciendis consequatur.