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
    line = entrada.readline()

    while line != "":
        listProd = line.split(";")
        dic[listProd[0]] = listProd[1]
        line = entrada.readline()
    return dic
    # fim da função

# Função que recebe um dicionário e retorna uma String
def f_saidaDados(dic):
    #declaração de variavel
    lista = []
    saida = ""

    for item in dic:
        lista.append(f'PRODUTO={item} PRECO={dic[item]}')
        
    lista.sort()
    
    for linha in lista:
        saida+=linha
    
    return saida