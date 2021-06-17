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

# Função que recebe um arquivo texto e retorna um dicionario
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

def f_saidaDados(dic):
    #declaração de variavel
    saida = ""

    for item in dic:
        saida += "PRODUTO=" + item + " PRECO=" + dic[item]
        
    return saida