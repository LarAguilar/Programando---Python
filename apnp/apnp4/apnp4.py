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

from funcs import f_lerArq, f_saidaDados

# função principal
def main():
    # declaracao de variaveis
    entrada = str()
    saida = str()
    nomeArqE = str()
    nomeArqS = str()
    dic = {}
    saidaDados = str()

    #entrada de dados
    nomeArqE = input()
    nomeArqS = input()

    #abre os arquivos de entrada e saida
    entrada = open(nomeArqE, "rt")
    saida = open(nomeArqS, "w")

    #processamento
    dic = f_lerArq(entrada)

    saidaDados = (f_saidaDados(dic))
    
    #saida de dados
    saida.write(saidaDados) #escreve os dados no arquivo de saida
    print(saidaDados)

    #fecha os arquivos
    entrada.close()
    saida.close()
    # Fim da função principal


if __name__ == "__main__":
    main()
