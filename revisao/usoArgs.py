#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# usoArgs.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

def main(args):
    #declaração de variáveis
    x = int(0)
    y = int(0)
    soma = int(0)

    x = int(args[1])
    y = int(args[2])
    print(args)
    soma = x + y
    print(soma)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))