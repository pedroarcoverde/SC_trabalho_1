from RSA import *
import base64, hashlib

# PARTE I

qtdPrimos = 1000   # Qtd de primos para teste de Sieve Eratorthenes
sieveEratosthenes(qtdPrimos)

# Gera duas tuplas com as chaves públicas e privadas distintas
p = geradorPeQ() 
while True:
    q = geradorPeQ()
    if (p != q):
        break

print(p)
print()
print(q)


# PARTE II

# PARTE III

# PARTE IV