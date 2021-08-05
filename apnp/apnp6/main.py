#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# main.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

from funcoes import *
import time, random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# programa principal
def main(): 
    # declaração de variáveis
    dic = {}
    lista1 = []
    lista2 = []
    lista3 = []
    metodos = []
    time_selection = []
    time_insertion = []
    time_sort = []
    tempo = []
    top = []
    lstNaoOrd = []
    dicBusca = {}

    # gera listas com números inteiros positivos e negativos gerados pseudoaleatoriamente
    # 10 un
    lista1 = random.sample(range(-10000, 10000), 10)
    lista2 = lista1.copy()
    lista3 = lista1.copy()

    # 100 un
    lista4 = random.sample(range(-10000, 10000), 100)
    lista5 = lista4.copy()
    lista6 = lista4.copy()

    # 1000 un
    lista7 = random.sample(range(-10000, 10000), 1000)
    lista8 = lista7.copy()
    lista9 = lista7.copy()

    # 10000 un
    lista10 = random.sample(range(-10000, 10000), 10000)
    lista11 = lista10.copy()
    lista12 = lista10.copy()

    # 100000 un
    lista13 = random.sample(range(-100000, 100000), 100000)
    lista14 = lista13.copy()
    lista15 = lista13.copy()

    # lista que será utilizada para métodos de busca
    lstNaoOrd = lista13.copy()

    metodos = ["Seleção", "Inserção", "Sort"]

######### processamento de tempo: métodos de ordenação #########

    # SelectionSort
    agora = time.process_time()
    selectionSort(lista1)
    tempo_decorrido = time.process_time() - agora
    time_selection.append(tempo_decorrido)

    # InsertionSort
    agora = time.process_time()
    insertionSort(lista2)
    tempo_decorrido = time.process_time() - agora
    time_insertion.append(tempo_decorrido)

    # Sort
    agora = time.process_time()
    lista3.sort()
    tempo_decorrido = time.process_time() - agora
    time_sort.append(tempo_decorrido)

    ### tam 100
    # SelectionSort
    agora = time.process_time()
    selectionSort(lista4)
    tempo_decorrido = time.process_time() - agora
    time_selection.append(tempo_decorrido)

    # InsertionSort
    agora = time.process_time()
    insertionSort(lista5)
    tempo_decorrido = time.process_time() - agora
    time_insertion.append(tempo_decorrido)

    # Sort
    agora = time.process_time()
    lista6.sort()
    tempo_decorrido = time.process_time() - agora
    time_sort.append(tempo_decorrido)

    ### tam 1000
    # SelectionSort
    agora = time.process_time()
    selectionSort(lista7)
    tempo_decorrido = time.process_time() - agora
    time_selection.append(tempo_decorrido)

    # InsertionSort
    agora = time.process_time()
    insertionSort(lista8)
    tempo_decorrido = time.process_time() - agora
    time_insertion.append(tempo_decorrido)

    # Sort
    agora = time.process_time()
    lista9.sort()
    tempo_decorrido = time.process_time() - agora
    time_sort.append(tempo_decorrido)

    ### tam 10000
    # SelectionSort
    agora = time.process_time()
    selectionSort(lista10)
    tempo_decorrido = time.process_time() - agora
    time_selection.append(tempo_decorrido)

    # InsertionSort
    agora = time.process_time()
    insertionSort(lista11)
    tempo_decorrido = time.process_time() - agora
    time_insertion.append(tempo_decorrido)

    # Sort
    agora = time.process_time()
    lista12.sort()
    tempo_decorrido = time.process_time() - agora
    time_sort.append(tempo_decorrido)

    ## tam 100000
    # SelectionSort
    agora = time.process_time()
    selectionSort(lista13)
    tempo_decorrido = time.process_time() - agora
    time_selection.append(tempo_decorrido)

    # InsertionSort
    agora = time.process_time()
    insertionSort(lista14)
    tempo_decorrido = time.process_time() - agora
    time_insertion.append(tempo_decorrido)

    # Sort
    agora = time.process_time()
    lista15.sort()
    tempo_decorrido = time.process_time() - agora
    time_sort.append(tempo_decorrido)
######### fim do processamento de tempo #########
    
    # define as chaves e valores no dicionário
    dic[metodos[0]] = time_selection
    dic[metodos[1]] = time_insertion
    dic[metodos[2]] = time_sort

    #saida de dados
    print(dic)

    top = ['Métodos' ,'10', '100', '1000', '10000', '100000']

    ######### SAIDA DE DADOS: tabela métodos de ordenação #########
    espaco = ' '
    print('-' * 83)
    print(f'{espaco:<13} {top[1]:>13} {top[2]:>13} {top[3]:>13} {top[4]:>13} {top[5]:>13}')
    print(('-' * 13) + ' ' + ('-' * 13)+ ' ' + ('-' * 13)+ ' ' + ('-' * 13)+ ' ' + ('-' * 13)+ ' ' + ('-' * 13))
    for key in dic:
        print(f'{key:<13} {dic[key][0]:>13,.5f} {dic[key][1]:>13,.5f} {dic[key][2]:>13,.5f} {dic[key][3]:>13,.5f} {dic[key][4]:>13,.5f}')
    print('-' * 83)
    ######### FIM SAÍDA TABELA #########

    ######### processamento do grafico #########
    tempo.append(dic[metodos[0]][4])
    tempo.append(dic[metodos[1]][4])
    tempo.append(dic[metodos[2]][4])

    # gera o grafico de barras
    plt.figure(figsize=(10,5))
    plt.bar(metodos, tempo, color='#6A5ACD') # define X e Y e a cor das barras
    plt.ylabel("Tempo decorrido") # Nome dos elementos do Y
    plt.xlabel("Método de Ordenação") #Nome dos elementos do X
    plt.title("Tempo X Método de Ordenação") #titulo da tabela
    plt.show() # mostra a tabela
    ###fim do processamento do grafico

    # a lstNaoOrd é uma copia da lista13, para otimizar o tempo de processamento do programa
    # lstNaoOrd = random.sample(range(-10000, 10000), 10000) #deve ser apagado no aqrv original
    lstOrd = lstNaoOrd.copy()
    lstOrd.sort()

    tmpBuscaSequencial = []
    tmpBuscaBinaria = []
    topBusca = []
    primeiraNaoOrd = lstNaoOrd[0]
    ultimaNaoOrd = lstNaoOrd[len(lstNaoOrd) - 1]
    meioNaoOrd = lstNaoOrd[len(lstNaoOrd)//2]
    foraLista = 135106
    topBusca = ["primeiro", "ultimo", "central", "nao existente"]

    # Busca Sequencial
    agora = time.process_time()
    buscaSequencial(lstNaoOrd, primeiraNaoOrd)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaSequencial.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstNaoOrd, ultimaNaoOrd)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaSequencial.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstNaoOrd, meioNaoOrd)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaSequencial.append(tempo_decorrido)

    agora = time.process_time()
    buscaSequencial(lstNaoOrd, foraLista)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaSequencial.append(tempo_decorrido)

    # Busca Binária

    agora = time.process_time()
    buscaBinaria(lstOrd, primeiraNaoOrd)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaBinaria.append(tempo_decorrido)

    agora = time.process_time()
    buscaBinaria(lstOrd, ultimaNaoOrd)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaBinaria.append(tempo_decorrido)

    agora = time.process_time()
    buscaBinaria(lstOrd, meioNaoOrd)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaBinaria.append(tempo_decorrido)

    agora = time.process_time()
    buscaBinaria(lstOrd, foraLista)
    tempo_decorrido = time.process_time() - agora
    tmpBuscaBinaria.append(tempo_decorrido)

    dicBusca["sequencial"] = tmpBuscaSequencial
    dicBusca["binária"] = tmpBuscaBinaria

    
    #SAIDA DE DADOS: tabela
    print(dicBusca)
    espaco = ' '
    print('-' * 72)
    print(f'{espaco:<13} {topBusca[0]:>13} {topBusca[1]:>13} {topBusca[2]:>13} {topBusca[3]:>16}')
    print(('-' * 13) + ' ' + ('-' * 13)+ ' ' + ('-' * 13)+ ' ' + ('-' * 13)+ ' ' + ('-' * 16))
    for key in dicBusca:
        print(f'{key:<13} {dicBusca[key][0]:>13,.5f} {dicBusca[key][1]:>13,.5f} {dicBusca[key][2]:>13,.5f} {dicBusca[key][3]:>16,.5f}')
    print('-' * 72)
    #FIM SAIDA DE DADOS tabela

    ###processamento do grafico
    barWidth = 0.25
    plt.figure(figsize=(10,5))
    r1 = np.arange(len(tmpBuscaBinaria))
    r2 = [x + barWidth for x in r1]
    plt.bar(r1, tmpBuscaSequencial, color='#6A5ACD', width=barWidth, label='Busca Sequencial')
    plt.bar(r2, tmpBuscaBinaria, color='#00BFFF', width=barWidth, label='Busca Binaria')

    # gera o grafico de barras 
    plt.ylabel("Tempo decorrido") # Nome dos elementos do Y
    plt.xlabel("Elemento a ser buscado") #Nome dos elementos do X
    plt.xticks([r + barWidth for r in range(len(tmpBuscaBinaria))], topBusca)
    plt.title("Tempo X Posição do Elemento") #titulo da tabela
    plt.legend()
    plt.show() # mostra a tabela
    ###fim do processamento do grafico

if __name__ == "__main__":
    main()
