# Alunos: PEDRO LÍSIAS VIANA ARCOVERDE ALVES 19/0036559
#         MARCELO PIANO                      20/******* 

# Cifra de Vigenère

#   Parte I: cifrador/decifrador
#     O cifrador recebe uma senha e uma mensagem que é cifrada segundo a cifra de Vigenère,
#     gerando um criptograma, enquanto o decifrador recebe uma senha e um criptograma que é
#     decifrado segundo a cifra de Vigenère, recuperando uma mensagem.
from unicodedata import normalize
import string

alfabeto = 'abcdefghijklmnopqrstuvwxyz '

letra_para_numero = dict(zip(alfabeto, range(len(alfabeto))))
numero_para_letra = dict(zip(range(len(alfabeto)), alfabeto))

def cifra(msg, chave):
    
    #limpa a mensagem (retira acentos, pontuação e coloca em maiscula)
    msg = msg.replace(' ', '').lower() #tira espaços e coloca em maiscula 
    msg = normalize('NFKD', msg).encode('ASCII','ignore').decode('ASCII') #tira acentos
    msg = msg.translate(str.maketrans('', '', string.punctuation)) #tira pontuação

    msg = list(msg) #transforma em lista

    # separa a mensagem em partes do tamanho da chave  
    msg_cifrada = ''
    split_msg = [msg[i:i + len(chave)] for i in range(0, len(msg), len(chave))]

    # converte a mensagem e a chave em numeros, cifra por Vigenère a mensagem
    for each_split in split_msg:
        i = 0
        for letra in each_split:
            numero = (letra_para_numero[letra] + letra_para_numero[chave[i]]) % len(alfabeto)
            msg_cifrada += numero_para_letra[numero]
            i += 1

    # retorna a mensagem cifrada
    return msg_cifrada


def decifra(msg_cifrada, chave):

    # separa a cifra em partes do tamanho da chave
    msg = ''
    split_msg_cifrada = [msg_cifrada[i:i + len(chave)] for i in range(0, len(msg_cifrada), len(chave))]

    # converte a mensagem e a chave em numeros
    for each_split in split_msg_cifrada:
        i = 0
        for letra in each_split:
            numero = (letra_para_numero[letra] - letra_para_numero[chave[i]]) % len(alfabeto)
            msg += numero_para_letra[numero]
            i += 1

    # retorna a mensagem decifrada
    return msg


#   Parte II: ataque de recuperação de senha por análise de frequência
#     Serão fornecidas duas mensagens cifradas (uma em português e outra em inglês) com senhas
#     diferentes. Cada uma das mensagens deve ser utilizada para recuperar a senha geradora do
#     keystream usado na cifração e então decifradas. 

def ataque (msg_cifrada, idioma):

    # para o ataque...
    chave_provavel = ''

    # retorna a chave provavel
    return chave_provavel



def main():

    while True:
        op = int(input("ESCOLHA UMA OPÇÃO:\n 1 - CIFRAR\n 2 - DECIFRAR\n 3 - ATACAR\n 4 - SAIR\n"))

        if ((op == 1) or (op == 2)):
                chave = list(input('\nDIGITE A CHAVE\n'))
                if (op == 1):
                        cifra_gerada = cifra(input('\nDIGITE A MENSAGEM A SER CIFRADA\n'), chave)
                        print("\nCIFRA GERADA:\n" + cifra_gerada)
                        input()

                elif (op == 2):
                        msg_obtida = decifra(list(input('\nDIGITE A MENSAGEM CIFRADA\n')), chave)
                        print("\nMENSAGEM OBTIDA:\n" + msg_obtida)
                        input()

        elif (op == 3):
                idioma = int(input('\nESCOLHA QUAL IDIOMA:\n 1 - INGLÊS\n 2 - PORTUGUÊS\n'))
                if ((idioma == 1) or (idioma == 2)):
                        chave_provavel = ataque(input('\nDIGITE A MENSAGEM CIFRADA\n'), idioma)
                        print("\nCHAVE PROVAVEL:\n" + chave_provavel)
                        input()

        elif (op == 4):
            break


main()

