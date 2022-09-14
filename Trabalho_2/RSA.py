import random
import math
from random import randint


# Verifica se d ≡ e−1 (mod λ(n)) que é se o resto da divisão de d por λ(n) for e**(-1)
def isModularMultiplicativeInversive(d,e,oDn):
    return print('fazer')

# Verifica se 2 números são coprimos
def isCoprime(x, y):
    if math.gcd(x, y) == 1:
        return True
    else:
        return False

# gera um número 'aleatório' de tamanho determinado em Bits


def geraNum(tamBits):
    num = random.randrange(2**(tamBits - 1) + 1, 2**tamBits - 1)
    return num


# verifica se é primo pelo método sieve Eratosthenes
listaPrimos = []


def sieveEratosthenes(n):
    primo = [True for i in range(n + 1)]
    p = 2
    while (p*p <= n):
        if (primo[p] == True):
            for i in range(p*p, n+1, p):
                primo[i] = False
        p += 1

    # Loop passando da lista de O(n) para uma lista APENAS com numeros primos
    for p in range(2, n+1):
        if primo[p]:
            listaPrimos.append(p)

# verifica se o numero gerado é primo e retorna


def geraPrimo(tamBits):
    while True:
        primo = geraNum(tamBits)

        # Divisao pelos primeiros numeros primos calculados pelo sieveEratosThenes
        for divisor in listaPrimos:
            if primo % divisor == 0 and divisor**2 <= primo:
                break
        else:
            return primo

########### implementar confirmação probalistica deq primo realmente é primo ##########################


def geradorPeQ():
    tamBits = 1024  # tamanho de P e Q em Bits
    pouq = gera_primo2(tamBits)
    return pouq


def geraE(oDn):

    while True:
        num = random.randrange(2, oDn - 1)
        if isCoprime(num, oDn):
            break

    return num


def geraD(e, oDn):
    
    while True:
        num = random.randrange(1, oDn - 1)
        if isModularMultiplicativeInversive(num, e, oDn):
            break
    
    return num


def cifracao(chave, textoplano):
    return


def decifracao(chave, cifra):
    return


def gera_primo2(tamanho):

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
    assert((2**k) * m == n - 1)

    for i in range(8):
        a = random.randrange(2, n)
        
        if pow(a, m, n) == 1:
            return False

        for x in range(k):
            if pow(a, 2**i * m, n) == n-1:
                return False

    return True
