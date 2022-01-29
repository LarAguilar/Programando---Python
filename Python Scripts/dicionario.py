pessoas = {'nome': 'Lara', 'idade': 18, 'sexo': 'F'}
'''print(f"A {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.values(): # aqui pode ser implementado o .keys() ou .items()
    print(k)'''

del pessoas['sexo']

pessoas['nome'] = "Jeredy" # modificar valores
pessoas['peso'] = 79.9 # acrescentar índices e seus valores

for k, v in pessoas.items():
    print(f"{k} = {v}")
