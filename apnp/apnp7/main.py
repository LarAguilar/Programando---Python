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

'''1.12.11. Uma universidade deseja fazer um levantamento a respeito de seu concurso vestibular. Para cada curso, é fornecido o seguinte conjunto de valores:
    o código do curso;
    o número de vagas;
    o número de candidatos do sexo masculino;
    o número de candidatos do sexo feminino. 
O último conjunto, para indicar fim de dados, contém o código do curso igual a zero. Fazer um algoritmo que:
    o calcule e escreva, para cada curso, o numero de candidatos por vaga e a porcentagem de candidatos do sexo feminino (escreva também o código correspondente do curso);
    o Determine o maior numero de candidatos por vaga e escreva esse número juntamente com o código do curso correspondente (supor que não haja empate);
    o calcule e escreva o total de candidatos.'''

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

    
def main():
    # declaração de variaveis
    dadosConcurso = {}
    totalInscritos = 0

    # processamento
    dadosConcurso, totalInscritos = geraDic()

    #saida de dados
    saidaDados(dadosConcurso, totalInscritos)



if __name__ == "__main__":
    main()