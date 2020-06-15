"""
Faça uma função IMC que receba dois argumentos: peso e altura, 
e retorne o valor do índice de massa corporal. Altere a sua solução do exercício 1 
da lista da Aula 4 para usar esta função
"""

def imc(peso, altura):
    return peso / (altura ** 2)

pesos = [56.3, 68.0, 96.3, 66.3, 70.9]
alturas = [1.70, 1.53, 1.90, 1.54, 1.87]
imcs = []

for i in range(len(pesos)):
    imcs.append(imc(pesos[i], alturas[i]))

print(f'lista de imcs: {imcs}')
