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


'''Leia este arquivo carregando os dados para um dicionário, onde a chave é o nome da capital e os demais dados deverão estar armazenados em uma lista. Use somente o nome da capital para montar a chave e descarte o número identificador da capital.

Grave este dicionário em um arquivo JSON.

Imprima um outro arquivo tipo texto onde os dados a serem impressos são os mesmos dados contidos na página do TabNet. Uma capital por linha. Estes dados deverão ser impressos de forma ordenada crescentemente pela taxa de analfabetismo.'''

from funcao import f_lerArq, f_saidaDados
import json

def main():
    #declaração de variaveis
    entrada = str()

    # entrada = input()

    # lê os dados do arquivo
    with open('entrada.txt', "rt") as entrada:
        #faz a leitura e o processamento das informações, retornando um dicionario 
        dic = f_lerArq(entrada)
    
    # escreve o dicionario "dic" em um arquivo json, com indentação 4
    with open('dados.json', 'w') as fp:
        json.dump(dic, fp, indent=4)

    # processamento da saida de dados
    f_saidaDados(dic)

    # fim do programa princiaal

if __name__ == "__main__":
    main()