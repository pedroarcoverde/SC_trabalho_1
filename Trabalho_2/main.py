import secrets
from RSA import *
from OAEP import oaep_encrypt, oaep_decrypt
import AES
import base64, hashlib
import sys
sys.setrecursionlimit(1500)

### PARTE I - GERAÇÃO DE CHAVES E CIFRAÇÃO ASSIMETRICA

## Gera duas tuplas com as chaves públicas e privadas

# Gera p e q distintos
p = geradorPeQ() 
while True:
    q = geradorPeQ()
    if (p != q):
        break

print(f"P = {p}\n\n")
print(f"Q = {q}\n\n")


# 'n' e 'O(n)'
n = p * q               #calculamos o modulo RSA (o que linka as chaves)
oDn = (p - 1) * (q - 1) #oDn é o totient

# Chaves públicas E e D
e = geraE(oDn)

d = geraD(e, oDn)

print(f"Suas chaves públicas são\n n = {n}\n e = {e}\n")
print(f"Suas chaves privadas são\n n = {n}\n d = {d}\n")

# Chaves em formato de tuplas
chavePublica = (e, n)
chavePrivada = (d, n)

# Leitura da mensagem
msg = input("Digite a mensagem:\n")



# PARTE II: Cifra simétrica 

#Gerando chave de assinatura
k1, k2 = secrets.token_bytes(16),secrets.token_bytes(16)

#print(int.from_bytes(b'\xbb\x0f|\xa9:_\xeci=\x0cL.\xe5#\xd4F', "little")) #para ver o número em decimal

chaveSessao = k1 + k2

"""
como fica 
b'\xecu\xe9;\xb1Cv_\xcc\x9cB\xbe]\x83\xb7\x90' = k1 
b'\x92\x81\x81\x9f\x03\xb0\x89)\xf4S\xb7\x15/\x0e\x16P' = k2
b'\xecu\xe9;\xb1Cv_\xcc\x9cB\xbe]\x83\xb7\x90\x92\x81\x81\x9f\x03\xb0\x89)\xf4S\xb7\x15/\x0e\x16P' = chaveSessao

"""

mensagemCifrada = AES.ctr(msg, k1, k2)




#msg = open('texto.txt', 'r').read() 
#print('Conteúdo do arquivo:')
#print(msg)



### PARTE II - ASSINATURA

### PARTE III

### PARTE IV