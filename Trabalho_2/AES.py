


def split(msg, tamanho):
    listaBlocos = []
    
    for indiceLetra in range(0, len(msg), tamanho):
        listaBlocos.append(msg[indiceLetra: indiceLetra + tamanho])

    return listaBlocos


def ctr(msg, k1, k2):    
    blocks = split(msg, 16)
