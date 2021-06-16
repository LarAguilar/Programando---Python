#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# apnp2.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

# função que gera uma string até a n-ésima linha
def f_geraString(n):
    # declaração de variavel
    armazena = ""
    n = n
    
    # processamento
    if n>0:
        for i in range(1, n+1):
            armazena += (str(i) + " ") * int(i) + "\n"
        return armazena
    else:
        return armazena

def main():
    # declaração de variaveis
    k = 0
    armazena = ""
    
    #entrada de dados
    k = int(input())

    #processamento
    while k>=0:
        armazena += f_geraString(k) + "\n"
        k = int(input())

    # output
    print(armazena)    

if __name__ == "__main__":
    main()