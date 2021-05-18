#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# revisao.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
#######################################
# Código fonte em Python 3
#######################################


def main():
    #declaração de variaveis
    #declarar TODAS as variáveis no main
    num1 = int(0)
    num2 = int(0)
    valor = float(0.0)
    nome = str("")
    logico = bool(False)
    lista = []

    #entrada de dados
    num1 = int(input()) #entrada interativa
    num2 = int(input()) #entrada nao interativa

    #processamento: soma dois numeros inteiros
    soma = num1 + num2

    #saída de dados
    print("Soma = %d " % (soma)) # % -> caracter de composição 
    # %d imprime apenas numero inteiro, caso esteja quebrado, ele arredonda
    print("Soma=", soma)
    print("Soma="+str(soma))

    valor=0.3333333333333
    nome="Lara"

    print("%d %f %s" % (soma, valor, nome))
    print("%d %.2f %s" % (soma, valor, nome))
    print(str(soma)+str(valor))

    
if __name__ == "__main__":
    main()