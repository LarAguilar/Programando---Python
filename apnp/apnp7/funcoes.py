#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# funcoes.py
#
# Copyright 2021
# Autor: Lara Aguilar de Amorim
#
############################
# Código fonte em Python 3
############################

# Função que gera e retorna um dicionario contendo as informações sobre os cursos do concurso publico da universidade
def geraDic():
    #declaração de variáveis
    dadosConcurso = dict()
    codCurso = int()
    qtdVagas = int()
    qtdMasculino = int()
    qtdFeminino = int()
    totalCandidatos = int()
    candidatosVaga = float()
    totalInscritos = 0

    # entrada de dados
    codCurso = int(input())

    #processamento de dados
    while codCurso > 0:
        # entrada de dados
        qtdVagas = int(input())
        qtdFeminino = int(input())
        qtdMasculino = int(input())

        #processamento
        totalCandidatos = qtdFeminino + qtdMasculino
        
        candidatosVaga = totalCandidatos / qtdVagas
        
        pctFeminino = qtdFeminino * 100 / totalCandidatos
        
        # adiciona os dados no dicionario
        dadosConcurso[codCurso] = [qtdVagas, qtdMasculino, qtdFeminino, candidatosVaga, pctFeminino]
        
        totalInscritos += totalCandidatos
        #entrada de dados

        codCurso = int(input())

    return dadosConcurso, totalInscritos


# funcao que recebe um dicionario e um inteiro e realiza uma saida de dados com esses dados
def saidaDados(dadosConcurso, totalInscritos):
    # declaração de variaveis
    maiorCV = []
    CVatual = 0
    # inicialização de variável
    maiorCV = [0, 0]

    for key in dadosConcurso:
        # inicialização de variável
        CVatual = dadosConcurso[key][3]

        # verifica o maior Candidato/Vaga
        if CVatual > maiorCV[1]:
            maiorCV = [key, CVatual]

        #saida de dados
        print(f'Curso={key} CV={CVatual:.2f} Perc Inscritos Feminino={dadosConcurso[key][4]:.2f}%')

    #saida de dados
    print(f'Maior Candidados/Vagas={maiorCV[1]:.2f} foi no curso={maiorCV[0]}')
    print(f'Total de inscritos={totalInscritos}')
