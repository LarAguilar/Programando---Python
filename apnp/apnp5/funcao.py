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
        dic[listProd[0]] = [float(listProd[1]), int(listProd[2]), int(listProd[3])]
        line = entrada.readline()
    
    return dic
    # fim da função

# lista[0] = "duda"


# Função que recebe um dicionário e retorna uma String
def f_saidaDados(dic):
    #declaração de variavel
    lista = []
    saida = ""

    #processamento
    for chave in dic:
        totalVendas = dic[chave][0] *dic[chave][2]
        lista.append(f'PRODUTO={chave} VENDAS={totalVendas:.2f}')

    lista.sort() # coloca os itens em ordem alfabetica
    for linha in lista:
        if linha == lista[len(lista) - 1]:
            saida+=linha
        else: 
            saida+=linha + "\n"
        
    return saida
    #fim da função

# Função que recebe um dicionario e o nome do produto, e retorna falso
def consultaProduto(dic, nomePdt):
    #processamento
    if nomePdt in dic:
        return True
    else:
        print("PRODUTO INEXISTENTE")
        return False
    # fim da função

# Função que recebe um dicionario, um valor inteiro e uma string
def consultaEstoque(dic, qtd, nomePdt):
    # declaração de variavel
    qtd_disponivel = int()

    #processamento
    qtd_disponivel = dic[nomePdt][1] - dic[nomePdt][2]
    if qtd <= qtd_disponivel and qtd > 0:
        dic[nomePdt][2] = dic[nomePdt][2] + qtd
        print("VENDA PROCESSADA")
    else:
        print("QUANTIDADE EM ESTOQUE INSUFICIENTE")
    return dic
    # fim da função

# Função que recebe um dicionario e retorna um dicionario
def vendas(dic):
    #declaração de variáveis
    nomePdt = str()
    qtd = int()

    # entrada de dados
    nomePdt = input()

    #processamento
    while nomePdt != "FIM":
        #entrada de dados
        qtd = int(input())
        if consultaProduto(dic, nomePdt):
            dic = consultaEstoque(dic, qtd, nomePdt)
        #entrada de dados
        nomePdt = input()

    return dic
    #fim da função