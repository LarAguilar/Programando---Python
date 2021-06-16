#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# apnp3.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

# importa a biblioteca com as funções
import opcoes

def main():
    # declaração de variáveis
    alt = ["a", "b", "c", "d", "e", "f"]
    saida = ""
    altEsc = ""
    caracter = ""

    #entrada de dados
    altEsc = input()

    #processamento
    while altEsc in alt:
        #entrada de dados
        caracter = input()
        
        #processamento
        if altEsc == alt[0]:
            saida += opcoes.f_AltA(caracter)
        elif altEsc == alt[1]:
            saida += opcoes.f_AltB(caracter)
        elif altEsc == alt[2]:
            saida += opcoes.f_AltC(caracter)
        elif altEsc == alt[3]:
            saida += opcoes.f_AltD(caracter)
        elif altEsc == alt[4]:
            saida += opcoes.f_AltE(caracter)
        else:
            saida += opcoes.f_AltF(caracter)
        
        #entrada de dados
        altEsc = input()
        
        # fim processamento

    #saida de dados
    print(saida)

if __name__ == "__main__":
    main()
# fim