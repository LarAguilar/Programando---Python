brasil = [] # cria uma lista
estado1 = {'uf': 'Espírito Santo', 'sigla': 'ES'} # cria um dicionario contendo informações sobre um estado
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1) # acrescenta na lista brasil o dicionario estado 1
brasil.append(estado2)

print(brasil) # imprime a lista contendo os dicionarios
print(brasil[0])
print(brasil[1]['uf'])

