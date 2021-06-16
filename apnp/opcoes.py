#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# opcoes.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

def f_AltA(caracter):
    # declaração de variaveis
    quantidade = 6
    saida = ""

    #processamento
    for i in range(quantidade):
        saida += str(caracter)*quantidade + "\n"
    return saida

def f_AltB(caracter):
    # declaração de variaveis
    quantidade = 6
    saida = ""
    
    #processamento
    for i in range(quantidade):
        saida += str(caracter)*(i+1) + "\n"
    return saida

def f_AltC(caracter):
    # declaração de variaveis
    espaco = " "
    quantidade = 6
    saida = ""

    #processamento
    for i in range(quantidade, 0, -1):
        for j in range(quantidade+1):
            if i > 5:
                saida += str(espaco) * (i-j) + str(caracter) * j + "\n"
    return saida

def f_AltD(caracter):
    # declaração de variaveis
    espaco = " "
    quantidade = 4
    qtd_caracter = 1
    saida = ""

    #processamento
    for i in range(quantidade, 0, -1):
        saida += str(espaco) * (i-1) + str(caracter) * (qtd_caracter) + "\n"
        qtd_caracter += 2
    
    #declaração de variavel
    qtd_caracter = 5
    
    #processamento
    for j in range(1, quantidade):
        saida += str(espaco) * (j) + str(caracter) * (qtd_caracter) + "\n"
        qtd_caracter -= 2
    return saida

def f_AltE(caracter):
    # declaração de variaveis
    quantidade = 6
    saida = ""
    
    #processamento
    for i in range(quantidade, 0, -1):
        saida += str(caracter) * i + "\n"
    return saida

def f_AltF(caracter):
    # declaração de variaveis
    espaco = " "
    quantidade = 6
    saida = ""
    
    #processamento
    for i in range(quantidade+1):
        for j in range(quantidade, 0, -1):
            if i > 5:
                saida += str(espaco) * (i-j) + str(caracter) * j + "\n"
    return saida