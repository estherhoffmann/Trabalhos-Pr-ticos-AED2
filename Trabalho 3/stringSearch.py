
def BadChar(string, tam_string):
    dist_alfabeto = [tam_string] * 10

    for i in range(1, tam_string+1):
        dist_alfabeto[int(string[i])] = tam_string - i
    return dist_alfabeto

def BoyerMoore(substring, tam_substring, string, tam_string):
    dist_alfabeto = BadChar(substring, tam_substring)
    ocorrencias = []
    k = tam_substring

    while k <= tam_string:
        r = 0
        while r < tam_substring and substring[tam_substring - r] == string[k -  r]:
            r += 1
        if r >= tam_substring:
            ocorrencias.append(k - tam_substring)
        if k == tam_string:
            k += 1
        else:
            k += dist_alfabeto[int(string[k + 1])] + 1
    return ocorrencias


nome_arq = input()
arquivo = open(nome_arq, 'r')
tam_string, tam_substring = map(int, arquivo.readline().split())

string = arquivo.readline().strip('\n')
string = '0'+string
substring = arquivo.readline().strip('\n')
substring = '0'+substring

ocorrencias = BoyerMoore(substring, tam_substring, string, tam_string)
for each in ocorrencias:
    print(each)
