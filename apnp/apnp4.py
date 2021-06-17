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

import funcoes

def main():
    # declaracao de variaveis
    entrada = str()
    saida = str()
    nomeArqE = str()
    nomeArqS = str()
    dic = {}

    #entrada de dados
    nomeArqE = input()
    entrada = open(nomeArqE, 'r')
    nomeArqS = input()
    saida = open(nomeArqS, "w")

    dic = funcoes.f_lerArq(entrada)

    saida.write(funcoes.f_saidaDados(dic))

    entrada.close()
    saida.close()

if __name__ == "__main__":
    main()
