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
    return modularInversion(e, oDn)[1] % oDn


# Implementação do algoritmo de euclides
def modularInversion(e, oDn):
    if e == 0:
        return (oDn, 0, 1)
    else:
        a, b, c = modularInversion(oDn % e, e)
        return (a, c - (oDn // e) * b, b) # back substitution


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