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

from funcao import vendas, f_lerArq, f_saidaDados
import json

# função principal
def main():
    # declaracao de variaveis
    entrada = str()
    saida = str()
    nomeArqE = str()
    nomeArqS = str()
    dic = {}
    saidaDados = str()
    dados = 0

    #entrada de dados
    # nomeArqE = input()
    # nomeArqS = input()

    #abre o arquivo de entrada
    with open("entrada.txt", "rt") as entrada:
        #processamento
        dic = f_lerArq(entrada)
        dic = vendas(dic)

    with open('dados.json', 'w') as fp:
        json.dump(dic, fp, indent=4)

    #abre o arquivo de saida
    with open("saida.txt", "wt") as saida:
        #saida de dados
        f_saidaDados(dic, saida)

    #Fim da função principal


if __name__ == "__main__":
    main()
