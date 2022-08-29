import sympy
import math

def carmichael(n):
    coprimos = [x for x in range(1, n) if math.gcd(x, n) == 1]
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimos):         #pow(A, B, C) efficiently computes pow(A, B) % C.
        k += 1
    return k

def isCoprime(x,y):
    if math.gcd(x,y) == 1:
        return True
    else:
        return False

def isModularMultiplicativeInversive(d,e,l):
    if (e * d) % l == 1:
        return True
    else:
        return False


# Parte I: Geração de chaves
# Geração de chaves (p e q primos com no mínimo de 1024 bits)

'''testar com os valores
    p = 61
    q = 53
    e = 17
    d = 413
'''

tamanhoMaximo = 10

while True:
    p = int(input(f"Escolha um número primo P maior que {tamanhoMaximo}:\n"))
    if p < tamanhoMaximo:
        print(f"P deve ser maior que {tamanhoMaximo}")
    elif not sympy.isprime(int(p)):
        print('q não é primo')
    else:
        break

while True:
    q = int(input(f"Escolha um número primo Q maior que {tamanhoMaximo}:\n"))
    if p < tamanhoMaximo:
        print(f"P deve ser maior que {tamanhoMaximo}")
    elif not sympy.isprime(int(q)):
        print("q não é primo!")
    else:
        break

n = p*q

lam = carmichael(n)

while True:
    e = int(input(f"Escolha um inteiro E que pertence ao intervalo 1 < e < {lam} e é coprimo de {lam}:\n"))
    if e < 1 and e > lam:
        print('Não pertence ao intervalo.')
    elif not isCoprime(e,lam):
        print(f'Não é coprimo de {lam}')
    else:
        break

while True:
    d = int(input(f"Escolha um inteiro D em que D x {e} = 1 mod({lam}):\n"))
    if not isModularMultiplicativeInversive(d,e,lam):
        print("Não é Modular Multiplicative Inversive.")
    else:
        break

print(f"Suas chaves públicas são n = {n}, e = {e}")
print(f"Suas chaves privadas são n = {n}, d = {d}")
