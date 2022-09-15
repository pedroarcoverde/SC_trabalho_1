import random
import math
from random import randint


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


def verificacaoprob(n):
    #Teste com abordagem probabilistica
    numeroMaxDivisoesP2 = 0
    ec = n-1
    while ec % 2 == 0:
            ec >>=1
            numeroMaxDivisoesP2 += 1
    assert(2**numeroMaxDivisoesP2 * ec == n-1)

    def funcParaRodada(testador):
            if pow(testador,ec,n) == 1:
                    return False
            for i in range(numeroMaxDivisoesP2):
                    if pow(testador,2**i*ec,n) == n-1:
                            return False
            return True

    #Numero de rodadas para verificacao
    nRodadas = 20
    for i in range(nRodadas):
            testador = random.randrange(2, n)
            if funcParaRodada(testador):
                    return False
    return True

def geradorPeQ():
    tamBits = 1024  # tamanho de P e Q em Bits
    
    while True:
        pouq = geraPrimo(tamBits)
        if not verificacaoprob(pouq):
            continue
        else:
            return pouq


def geraE(oDn):
    # Calcula o expoente E para Chave PUBLICA
    # Escolhe aleatoriamente um numero que seja 1 < E < o(N) e se o MDC(e,oDn) == 1
    while True:
        num = random.randrange(2, oDn)
        if math.gcd(oDn, num) == 1:
            break

    return num


def geraD(e, oDn):
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

