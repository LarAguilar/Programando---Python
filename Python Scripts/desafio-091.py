'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado'''

from random import randint
jogadores = []
jogador = dict()
for i in range(4):
    jogador['dado'] = randint(1,6)
    jogadores.append(jogador.copy())

for i in range(1, len(jogadores)+1):



