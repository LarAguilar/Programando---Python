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

def main():
    print("a")

    entrada = open('entrada.txt', 'r')
    
    texto = entrada.readline()

    print(texto)

    entrada.close()


if __name__ == "__main__":
    main()
