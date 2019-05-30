#   Segundo Trabalho Prático - Algoritmos e Estrutura de Dados 2
#   Nome: Esther Calderan Hoffmann
#   Curso: Ciência da Computação
#   RA: 743529

qnt_inversoes = 0

def dividir(vetor):
    return (vetor[: len(vetor) // 2], vetor[len(vetor) // 2 :])

def merge(esquerda, direita):

    indice_esquerda = 0
    indice_direita = 0
    vetor_ordenado = []
    global qnt_inversoes

    while indice_esquerda < len(esquerda) and indice_direita < len(direita):

        if esquerda[indice_esquerda] <= direita[indice_direita]:
            vetor_ordenado.append(esquerda[indice_esquerda])
            indice_esquerda += 1
        else:
            vetor_ordenado.append(direita[indice_direita])
            indice_direita += 1
            qnt_inversoes += len(esquerda) - indice_esquerda

    if indice_esquerda < len(esquerda):
        vetor_ordenado.extend(esquerda[indice_esquerda:])
    elif indice_direita < len(direita):
        vetor_ordenado.extend(direita[indice_direita:])

    return vetor_ordenado

def contarInversoes_mergeSort(vetor):
    if vetor is None:
        return None

    if len(vetor) < 2:
        return vetor

    esquerda, direita = dividir(vetor)

    return merge(contarInversoes_mergeSort(esquerda), contarInversoes_mergeSort(direita))



tamanho_vetor = int(input())
vetor = input().split()
vetor = [ int(elemento) for elemento in vetor ]

contarInversoes_mergeSort(vetor)
print(qnt_inversoes)
