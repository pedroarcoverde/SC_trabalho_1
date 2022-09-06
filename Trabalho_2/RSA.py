import random
import math

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
    pouq = geraPrimo(tamBits)
    return pouq


def geraE(oDe):

    while True:
        num = random.randrange(1, oDe - 1)
        if isCoprime(num, oDe):
            break

    return num


def geraD(e, oDe):
    d = 1
    return d


def cifracao(chave, textoplano):
    return


def decifracao(chave, cifra):
    return
