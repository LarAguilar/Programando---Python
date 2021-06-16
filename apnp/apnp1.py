#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# apnp1.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

# função que verifica se o numero é impar ou par
def f_verifica(n):
    if n % 2 == 0:
        return True
    else:
        return False

def main():
    # declaração de variaveis
    n = 0
    verificacao = False
    
    # entrada de dados
    n = int(input())

    # processamento
    verificacao = f_verifica(n) # chama a função que verifica se o numero é impar ou par
    
        # saida de dados
    if verificacao == True:
        print("N = %d EH PAR" % n)
    else:
        print("N = %d EH IMPAR" % n)
    
    # fim do processamento

if __name__ == "__main__":
    main()