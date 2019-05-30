#   Primeiro Trabalho Prático - Algoritmos e Estrutura de Dados 2
#   Nome: Esther Calderan Hoffmann
#   Curso: Ciência da Computação
#   RA: 743529

def funcao_hash(palavra, tam_Hash):
    soma = 0
    for letra in palavra:
        soma = ((soma*127) + ord(letra)) % tam_Hash
    return soma 

def reHash(palavra, tam_Hash):
    soma = 0
    for letra in range(len(palavra)):
        soma = ((soma*41) + ord(palavra[letra])) % tam_Hash
    return soma


def busca_hash(palavra, hash_table, tam_hash_table):
    chave = funcao_hash(palavra, tam_hash_table)
    
    while(hash_table[chave] != None):
        if hash_table[chave][0] == palavra:
            return hash_table[chave][1]
        else: 
            chave = (chave + reHash(palavra, tam_hash_table)) % (tam_hash_table)
    return None #não esta na hash


def insere_hash(hash_table, valor, palavra, tam_hash_table):
   
    if(busca_hash(palavra, hash_table, tam_hash_table) != None):
        print('erro ao inserir')
        return None #palavra já está na hash

    chave = funcao_hash(palavra, tam_hash_table)
    while(hash_table[chave] is not None):
        chave = (chave + reHash(palavra, tam_hash_table)) % (tam_hash_table)

    hash_table[chave] = [palavra, valor]
    return hash_table


valores_iniciais = input().split()
qnt_palavras = int(valores_iniciais[0])
qnt_participantes = int(valores_iniciais[1])
tam_hash_table = 5 * qnt_palavras
hash_table = [None] * tam_hash_table


for palavra  in range(0, qnt_palavras):
    palavra_e_valor = input()
    palavra, valor = palavra_e_valor.split()
    valor = int(valor)    
    hash_table = insere_hash(hash_table, valor, palavra, tam_hash_table)


for aluno in range(0, qnt_participantes):
    texto = input().split()
    pontos = 0
    for each_word in texto:
        resultado_busca = busca_hash(each_word, hash_table, tam_hash_table)
        if resultado_busca == None:
            pontos -= 10
        else:
            pontos += resultado_busca
    ponto_de_separacao = input()
    print(pontos)

