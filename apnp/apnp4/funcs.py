#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# apnp4.py
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
    line = entrada.readline().strip()

    while line != "":
        listProd = line.split(";")
        print(dic)
        dic[listProd[0]] = listProd[1]
        line = entrada.readline()
    
    return dic
    # fim da função

# lista[0] = "duda"


# Função que recebe um dicionário e retorna uma String
def f_saidaDados(dic):
    #declaração de variavel
    lista = []
    saida = ""

    for chave in dic:
        lista.append(f'PRODUTO={chave} PRECO={dic[chave]}')

    lista.sort()
    ["Produto= A borboleto Preco=42.56", "produto= dnaslnxps preco=4566"]
    for linha in lista:
        saida+=linha
        
    return saida