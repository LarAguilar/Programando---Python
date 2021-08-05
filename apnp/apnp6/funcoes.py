#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# funcoes.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################


'''A função faz a busca sequencial de um elemento dentro de uma lista
RECEBE uma lista e o elemento a ser procurado
RETORNA a posicao do elemento na lista'''
def buscaSequencial(lista, elemento):
    #declaração de variavel
    pos = int(0)
    i = int(0)

    # processamento
    pos = -1
    while i < len(lista) and pos == -1:
        if lista[i] == elemento:
            pos = i
        i += 1
    # fim processamento
    return pos
    # fim da funcao


'''A função faz a busca binária de um elemento dentro de uma lista ordenada
RECEBE uma lista ordenada e o elemento a ser procurado
RETORNA a posicao do elemento na lista'''
def buscaBinaria(lista, elemento):
    # declaracao de variavel
    pos = int(0)
    inicio = int(0)
    meio = int(0)
    fim = len(lista) - 1
    pos = -1

    #processamento
    while inicio <= fim and pos == -1:
        meio = (inicio + fim) // 2

        if elemento == lista[meio]:
            pos = meio
        elif elemento < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    # fim do processamento
    return pos
    #fim da funcao

'''A função identifica o menor elemento dentro de uma lista
RECEBE uma lista
RETORNA a posição do menor elemento da lista'''
# def menorElemento(lista):
#     # declaração de variavel
#     menor = lista[0]

#     #processamento
#     for i, elemento in enumerate(lista[1:], start=1):
#         if elemento < menor:
#             menor = elemento
#             posMenor = i
#     #fim do processamento    
#     return posMenor
#     # fim da funcao


'''Função ordena uma lista através do método de Seleção
RECEBE uma lista e RETORNA a lista ordenada'''
def selectionSort(lista):
    #processamento
    for i in range(len(lista) - 1):
        posMenor = i

        for k, elemento_analisado in enumerate(lista[i+1:], start=i+1):
            if elemento_analisado < lista[posMenor]:
                posMenor = k

        lista[posMenor], lista[i] = lista[i], lista[posMenor]
    #fim do processamento
    return lista 
    #fim da funcao


'''Função ordena uma lista através do método de Inserção
RECEBE uma lista e RETORNA a lista ordenada'''
def insertionSort(lista):
    #processamento
    for i, elemento in enumerate(lista[:], start=0):
        j = i - 1
        while j >= 0 and lista[j] > elemento:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = elemento
    #fim processamento
    return lista
    #fim da funcao

# '''Função ordena uma lista através do método Merge
# RECEBE uma lista e valores padrão da posição de inicio e fim,
# SEPARA a lista em partes e realiza o merge'''
# def mergeSort(lista, inicio=0, fim=None):
#     if fim == None:
#         fim = len(lista)
#     if fim - inicio > 1:
#         meio = (fim + inicio) // 2
#         mergeSort(lista, inicio, meio)
#         mergeSort(lista, meio, fim)
#         merge(lista, inicio, meio, fim)

# '''Recebe uma lista, a posição de inicio, meio e fim
# e realiza o merge das partes da lista'''
# def merge(lista, inicio, meio, fim):
#     left = lista[inicio:meio]
#     right = lista[meio:fim]

#     top_left, top_right = 0, 0

#     for k in range(inicio, fim):
#         if top_left >= len(left):
#             lista[k] = right[top_right]
#             top_right += 1
#         elif top_right >= len(right):
#             lista[k] = left[top_left]
#             top_left += 1
#         elif left[top_left] < right[top_right]:
#             lista[k] = left[top_left]
#             top_left += 1
#         else:
#             lista[k] = right[top_right]
#             top_right += 1
