
def intercala(vetor, primeiro, meio, ultimo):
    qnt_inversoes = 0

    primeiro = int(primeiro)
    meio = int(meio)
    ultimo = int(ultimo)

    indice_subvetor1 = int(primeiro)
    indice_subvetor2 = int(meio)
    k = 0
    tamanho = int(ultimo - primeiro)
    aux_ordenado = [None] * tamanho

    while(indice_subvetor1 < meio and indice_subvetor2 < ultimo):
        if (vetor[indice_subvetor1] <= vetor[indice_subvetor2]):
            aux_ordenado[k] = vetor[indice_subvetor1]
            k += 1
            indice_subvetor1 += 1

        else:
            aux_ordenado[k] = vetor[indice_subvetor2]
            k += 1
            indice_subvetor2 += 1
            qnt_inversoes += meio - indice_subvetor1

    while(indice_subvetor1 < meio):
        aux_ordenado[k] = vetor[indice_subvetor1]
        k += 1
        indice_subvetor1 += 1

    while(indice_subvetor2 < ultimo):
        aux_ordenado[k] = vetor[indice_subvetor2]
        k += 1
        indice_subvetor2 += 1

    for k in range(0, tamanho):
        vetor[primeiro + k] = aux_ordenado[k]

    return qnt_inversoes

def contarInversoesR(vetor, primeiro, ultimo):
    qnt_inversoes = 0
    if (ultimo - primeiro > 1):
        meio = (primeiro + ultimo)/2

        qnt_inversoes += contarInversoesR(vetor, primeiro, meio)
        qnt_inversoes += contarInversoesR(vetor, meio, ultimo)
        qnt_inversoes += intercala(vetor, primeiro, meio, ultimo)
    return qnt_inversoes

def contarInversoes(vetor, tamanho):
    return contarInversoesR(vetor, 0, tamanho)



tamanho_vetor = int(input())
vetor = input().split()
vetor = [ int(elemento) for elemento in vetor ]
qnt = contarInversoes(vetor, tamanho_vetor)
print(qnt)
