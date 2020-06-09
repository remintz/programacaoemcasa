'''
(listas e comando ‘for’) Dadas duas listas:
pesos = [56.3, 68.0, 96.3, 66.3, 70.9] e alturas = [1.70, 1.53, 1.90, 1.54, 1.87]
construa uma terceira lista imc contendo o cálculo do índice de massa corporal usando 
a fórmula imc[i] = peso[i] / altura[i] ** 2, ou seja, o valor da lista imc no índice 
‘i’ deve ser igual à fórmula do imc aplicada no índice ‘i’ da lista peso e no índice 
‘i’ da lista altura.
'''

pesos = [56.3, 68.0, 96.3, 66.3, 70.9]
alturas = [1.70, 1.53, 1.90, 1.54, 1.87]
imc = []

for i in range(len(pesos)):
    imc.append(pesos[i] / alturas[i] ** 2)

print(f'lista de imcs: {imc}')
