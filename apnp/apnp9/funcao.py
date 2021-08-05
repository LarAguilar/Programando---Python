#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# funcao.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

def f_lerArq(entrada):
    #declaracao de variaveis
    dic = dict()
    listProd = list()
    line = ""

    #processamento
    line = entrada.readline()

    #organiza os dados separados por ; em um dicionario
    while line != "":
        listProd = line.split(";")
        dic[listProd[0]] = [float(listProd[1]), int(listProd[2]), int(listProd[3])]
        line = entrada.readline()
    
    return dic
    # fim da função


# Função que recebe um dicionário e o retorna ordenado de acordo com os valores
def f_saidaDados(dic):
    #declaração de variavel
    sortedDict = {}
    linha = str()
    
    #Coloca os itens em ordem crescente de acordo com os valores do dicionario
    sortedDict = sorted(dic.items(), key=lambda x: x[1])
        
    # escreve no arquivo saida.txt os dados ordenados separados por ;
    with open('saida.txt', 'w') as saida:
        for chave, elemento in sortedDict:
            linha = f'{chave};{elemento[0]};{elemento[1]};{elemento[2]}'
            saida.write(linha + '\n')

            #saida de dados
            print(linha)

    
    return sortedDict
    #fim da função