import random

# gera um número 'aleatório' de tamanho determinado em Bits
def geraNum(tamBits):
    num = random.randrange(2**(tamBits - 1) + 1, 2**tamBits - 1)
    return num

# verifica se é primo pelo método sieve Eratosthenes
listaPrimos = []
def sieveEratosthenes(n):
    primo = [True for i in range(n + 1)]

# verifica se o numero gerado é primo e retorna
def geraPrimo(tamBits):
    while True:
        primo = geraNum(tamBits)

        #Divisao pelos primeiros numeros primos calculados pelo sieveEratosThenes
        for divisor in listaPrimos:
                if primo % divisor == 0 and divisor**2 <= primo:
                        break
        else:
            return primo

########### implementar confirmação probalistica deq primo realmente é primo ##########################


def geradorPeQ():
    tamBits = 1024 # tamanho de P e Q em Bits
    pouq = geraPrimo(tamBits)
    return pouq








def cifracao(chave, textoplano):
    return

def decifracao(chave, cifra):
    return
