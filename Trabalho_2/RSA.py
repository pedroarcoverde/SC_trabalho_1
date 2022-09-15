import random
import math

########### implementar confirmação probalistica deq primo realmente é primo ##########################
# Nova implementação para gerar o primo
def gera_primo(tamanho):

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
    pouq = gera_primo(tamBits)
    return pouq


def geraE(oDn):

    while True:
        num = random.randrange(2, oDn)
        if math.gcd(oDn, num) == 1:
            break

    return num

def geraD(e, oDn):
    return modularInversion(e, oDn)[1] % oDn
    

def modularInversion(e, oDn):
    if e == 0:
        return (oDn, 0, 1)
    else:
        a, b, c = modularInversion(oDn % e, e)
        return (a, c - (oDn // e) * b, b)


def cifracao(chave, textoplano):
    return


def decifracao(chave, cifra):
    return

