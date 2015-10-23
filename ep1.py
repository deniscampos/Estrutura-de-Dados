#!-*- conding: utf8 -*-
import random
import time
import sys

sys.setrecursionlimit(10000)

def imprimir_tabela():
    tabela = """
|----------------------- [EP1 - Vale a pena ordenar?] ----------------------|
|                                                                           |
|   Estrutura de Dados - FATEC                          3º ADS A - Manhã    |
|   Aluno:   Denis Campos de Paula                                          |
|                                                                           |
|---------------------------------------------------------------------------|
|       |       Tempo de Ordenação       |          Número de Buscas        |
|   n   |-------------------------------------------------------------------|
|       | Inserção Seleção Merge. Quick. | Inserção Seleção Merge. Quick.   |
|-------|-------------------------------------------------------------------|"""
    return tabela


def imprimir_linha(n, tempos, passos):
    print("|%6d |%8.2f  %6.2f  %5.2f  %5.2f  |%8d  %6d  %5d  %5d    |" %(n, tempos[0], tempos[1], tempos[2], tempos[3], passos[0], passos[1], passos[2], passos[3]))



def gerar_vetor_aleatorio(num):
    v = []
    while len(v) < num:
        n = random.randint(0, num)
        if n not in v:
            v.append(n)
    return v

def gerar_vetor():
    v = []
    for i in range(1, 70000):
        v.append(i)
    return v


# -------  Busca  -------
def busca_sequencial(n, v):
    for i in v:
        if i == n:
            return v.index(i)
    return -1

def busca_binaria(n, v):
    while len(v) > 1:
        m = len(v) // 2
        if v[m] > n:
            v = v[ : m]
        else:
            v = v[m: ]

    return v


# -------  ordenação  -------
def insercao(v):
    if len(v) <= 1: 
        return v
    
    for n in range(1, len(v)):
        for i in range(n-1, -1, -1):
            if v[i+1] < v[i]:
                v[i+1], v[i] = v[i], v[i+1]
            else:
                break
    return v


def selecao(v):    
    if len(v) <= 1: 
        return v
    
    for n in range(0, len(v)):
        for i in range(n+1, len(v)):
            if v[i] < v[n]:
                v[n], v[i] = v[i], v[n]
    return v


def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)


def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivo = lista[0]
    iguais  = [x for x in lista if x == pivo]
    menores = [x for x in lista if x <  pivo]
    maiores = [x for x in lista if x >  pivo]
    return quicksort(menores) + iguais + quicksort(maiores)


# -------  Calculos de tempo e busca  -------

def calcular_tempo_ordenacao(funcao, vetor):
    inicio = time.time()
    funcao(vetor)
    fim = time.time()
    return fim - inicio


def calcular_tempo_busca(funcao, numero, vetor):
    inicio = time.time()
    funcao(numero, vetor)
    fim = time.time()
    return fim - inicio


def calcular_buscas(v, tempo_ordenacao, numero):
    tempo_sequencial = 0
    tempo_binaria = tempo_ordenacao
    passos = 0
    
    while(tempo_binaria >= tempo_sequencial):
        tempo_binaria += calcular_tempo_busca(busca_binaria, numero, v)
        tempo_sequencial += calcular_tempo_busca(busca_sequencial, numero, v)
        passos += 1

    return passos



print("Calculando, aguarde...")
tempos = []
passos = []

num = 2000

inicio = time.time()
while(time.time() - inicio < 30):

    funcoes = [insercao, selecao, mergesort, quicksort]

    aux_tempos = []
    aux_passos = []

    numero = random.randint(0, num * 2)
    for f in funcoes:
        vetor_gerado = gerar_vetor_aleatorio(num)

        aux_tempos.append(calcular_tempo_ordenacao(f, vetor_gerado))
        aux_passos.append(calcular_buscas(vetor_gerado, aux_tempos[funcoes.index(f)], numero))

    tempos.append(aux_tempos)
    passos.append(aux_passos)

    num += 2000

print(imprimir_tabela())
for i in range(len(tempos)):
    n = 2000 * (i + 1)
    t = tempos[i]
    p = passos[i]
    imprimir_linha(n, t, p)
print("|-------|-------------------------------------------------------------------|")



