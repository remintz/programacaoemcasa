'''
1. Dada a lista numeros=[2,5,7,1,13,9,8,5,3,6,2,12,3]
a. Calcule a média dos valores da lista.
b. Informe o maior e o menor número da lista.
c. Separe-a em duas listas “pares” e “impares” sem números repetidos
d. Separe-a em duas listas: uma com os números acima da média e outra com os
números abaixo ou igual à média
'''

numeros = [2,5,7,1,13,9,8,5,3,6,2,12,3]

# 1.a
soma = 0
for i in range(len(numeros)):
    soma = soma + numeros[i]
media = soma / len(numeros)
print(f'a média é {media}')

# 1.b
print(f'o maior número é o {max(numeros)}')
print(f'o menor número é o {min(numeros)}')

# 1.c
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        if not numero in pares:
            pares.append(numero)
    else:
        if not numero in impares:
            impares.append(numero)
pares.sort()
impares.sort()
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')

# 1.d
abaixo = []
acima = []
for numero in numeros:
    if numero < media:
        if not numero in abaixo:
            abaixo.append(numero)
    else:
        if not numero in acima:
            acima.append(numero)
abaixo.sort()
acima.sort()
print(f'Os números abaixo da média são {abaixo}')
print(f'Os números acima da média são {acima}')

