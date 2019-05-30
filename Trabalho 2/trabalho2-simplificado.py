#   Segundo Trabalho Prático - Algoritmos e Estrutura de Dados 2
#   Nome: Esther Calderan Hoffmann
#   Curso: Ciência da Computação
#   RA: 743529

def dividir(vetor):
    return (vetor[: len(vetor) // 2], vetor[len(vetor) // 2 :])

def merge(esquerda, direta):

    indice_esquerda = 0
    indice_direta = 0
    vetor_ordenado = []

    while indice_esquerda < len(esquerda) and indice_direta < len(direta):
        if esquerda[indice_esquerda] <= direta[indice_direta]:
            vetor_ordenado.append(esquerda[indice_esquerda])
            indice_esquerda += 1
        else:
            vetor_ordenado.append(direta[indice_direta])
            indice_direta += 1

    if indice_esquerda < len(esquerda):
        vetor_ordenado.extend(esquerda[indice_esquerda:])
    elif indice_direta < len(direta):
        vetor_ordenado.extend(direta[indice_direta:])

    return vetor_ordenado, indice_direta

def contarInversoes_mergeSort(vetor):
    if vetor is None:
        return None

    if len(vetor) < 2:
        return vetor

    esquerda, direta = dividir(vetor)

    return merge(mergeSort(esquerda), mergeSort(direta))


#tamanho_vetor = int(input())
#vetor = input().split()
#vetor = [ int(elemento) for elemento in vetor ]

#qnt_inversoes = 0
