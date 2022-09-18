import random
import math

def geraPrimo(tamanho):

    while True:
        x = random.randrange(1 << (tamanho-1), (1 << tamanho) - 1)
        if ehPrimo(x):
            return x

def ehPrimo(n):    
    k = 0
    m = n-1

    while m % 2 == 0:
        k += 1
        m>>=1
       
    if (2**k) * m != n - 1:
        return False

    for i in range(8):
        a = random.randrange(2, n)
        
        if pow(a, m, n) == 1:
            return False

        for x in range(k):
            if pow(a, 2**i * m, n) == n-1:
                return False

    return True


def geradorPeQ():
    tamBits = 1024  # tamanho de P e Q em Bits
    pouq = geraPrimo(tamBits)
    return pouq


def geraE(oDn):

    while True:
        num = random.randrange(1, oDn)
        if math.gcd(oDn, num) == 1:
            break

    return num

def geraD(e, oDn):
    return modularInversion(e, oDn)[1] % oDn

# Implementação do algoritmo de euclides
def modularInversion(e, oDn):
    if e == 0:
        return (oDn, 0, 1)
    else:
        a, b, c = modularInversion(oDn % e, e)
        return (a, c - (oDn // e) * b, b) #back substitution


def cifracao(chave, txtplano):
    key, n = chave
    #Conversao por a^b mod m
    cifra = [pow(ord(char),key,n) for char in txtplano]
    return cifra


def decifracao(chave, cifra):
    key, n = chave
    #Conversao das letras cifradas baseada na chave
    aux = [str(pow(char,key,n)) for char in cifra]
    txtplano = [chr(int(char2)) for char2 in aux]
    return ''.join(txtplano)

