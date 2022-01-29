'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

alunos = []
aluno1 = dict()
aluno1['Nome'] = input('Nome: ')
aluno1['Media'] = float(input('Média: '))
alunos.append(aluno1)

for i in alunos:
    if i['Media'] >= 7:
        i['Situacao'] = 'aprovado'
    else:
        i['Situacao'] = 'reprovado'
    for k, v in i.items():
        print(f'{k} é igual a {v}')

