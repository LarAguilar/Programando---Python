#!/usr/bin/env python3 -> usar no ubuntu
# -*- coding: utf-8 -*- -> usar no ubuntu
# 
# aquecimento.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

def main():
    #declaração de variaveis
    n = int(0)
    m = str(0)

    #entrada de dados
    n = int(input())
    
    #converte tipo primitivo
    n = str(n)

    #processamento
    m = n[::-1] # coloca as variaveis de tras pra frente
    
    #conversão do tipo primitivo de dados
    n = int(n)
    m = int(m)

    #saida de dados
    print("N = %d -> M = %d" % (n, m))

if __name__ == "__main__":
    main()