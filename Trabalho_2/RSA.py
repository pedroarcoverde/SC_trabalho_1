import random
import math
from hashlib import sha3_256
import sys
sys.setrecursionlimit(1500)

import OAEP


def geraPrimo(tamanho):

    while True:
        x = random.randrange(1 << (tamanho-1), (1 << tamanho) - 1)
        if ehPrimo(x):
            return x

# Teste de primalidade Miller-Rabin
# def ehPrimo(n):    
#     k = 0
#     m = n-1

#     while m % 2 == 0:
#         k += 1
#         m >>= 1
       
#     if (2**k) * m != n - 1:
#         return False

#     for i in range(8):
#         a = random.randrange(2, n)
        
#         if pow(a, m, n) == 1:
#             return False

#         for x in range(k):
#             if pow(a, 2**i * m, n) == n-1:
#                 return False

#     return True

def ehPrimo(n):
    k = 0
    m = n - 1

    while m % 2 == 0:
        k += 1
        m >>= 1

    for i in range(40):

        a = random.randrange(2, n - 1)
        x = pow(a, m, n)

        if x == 1 or x == n - 1:
            continue

        for i in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        return False

    return True


def geraE(oDn):
    while True:
        e = random.randrange(2, oDn)
        if math.gcd(oDn, e) == 1:
            break
    return e


def geraD(e, oDn):
        #Bruxaria realizada durante a madrugada, apenas eu (Dur4ndal) e Jesus cristo sabemos o que rolou aqui. #Shalom
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        tmp = oDn

        while e>0:
                tmp1 = tmp//e
                tmp2 = tmp - tmp1*e
                tmp = e
                e = tmp2

                x = x2 - tmp1 * x1
                y = d - tmp1 * y1

                x2 = x1
                x1 = x
                d = y1
                y1 = y
        if tmp == 1:
                return d+oDn


def gera_chaves():

    p = geraPrimo(1024)
    q = geraPrimo(1024)
    n = p * q
    oDn = (p - 1) * (q - 1)

    e = geraE(oDn)
    d = geraD(e, oDn)

    chave_publica = (n, e)
    chave_privada = (n, d)

    return chave_publica, chave_privada


def rsa(chave, msg):
    n, exp = chave
    k = (n.bit_length() + 7) // 8
    m = int.from_bytes(msg, "big")
    c = pow(m, exp, n)

    return c.to_bytes(k, "big")


def cifra(chave, msg):
    txt_cifrado = OAEP.cifra_oaep(chave[0], msg)

    return rsa(chave, txt_cifrado)


def decifra(chave, txt_cifrado):
    msg = rsa(chave, txt_cifrado)

    return OAEP.decifra_oaep(chave[0], msg)


def assina(chave_privada, data):
    hash = sha3_256(data).digest()

    return rsa(chave_privada, hash)


def verifica_assinatura(chave_publica, data, assinatura):
    hash = sha3_256(data).digest()
    assinatura_confere = rsa(chave_publica, assinatura)[-32:] == hash

    return assinatura_confere