from decimal import *
getcontext().prec = 10
valor = Decimal(input('Qual é o valor em Reais? '))
print('Valor: ', valor)

notas_100 = int(valor / 100)
print('Notas de 100: ', notas_100)

valor = valor % Decimal(100)

print('Valor: ', valor)
notas_50 = int(valor / 50)
print('Notas de 50: ', notas_50)

valor = valor % Decimal(50)

print('Valor: ', valor)
notas_20 = int(valor / 20)
print('Notas de 20: ', notas_20)

valor = valor % Decimal(20)

print('Valor: ', valor)
notas_10 = int(valor / 10)
print('Notas de 10: ', notas_10)

valor = valor % Decimal(10)

print('Valor: ', valor)
notas_5 = int(valor / 5)
print('Notas de 5: ', notas_5)

valor = valor % Decimal(5)

print('Valor: ', valor)
notas_2 = int(valor / 2)
print('Notas de 2: ', notas_2)

valor = valor % Decimal(2)

print('Valor: ', valor)
moedas_1 = int(valor / 1)
print('Moedas de 1: ', moedas_1)

valor = valor % Decimal(1)

print('Valor: ', valor)
moedas_50 = int(valor / Decimal(0.50))
print('Moedas de 0.50: ', moedas_50)

valor = valor % Decimal(0.5)

moedas_25 = int(valor / Decimal(0.25))
print('Moedas de 0.25: ', moedas_25)

valor = valor % Decimal(0.25)

print('Valor: ', valor)
moedas_10 = int(valor / Decimal(0.10))
print('Moedas de 0.10: ', moedas_10)

valor = valor % Decimal(0.1)

print('Valor: ', valor)
moedas_5 = int(valor / Decimal(0.05))
print('Moedas de 0.05: ', moedas_5)
print('Valor: ', valor)

valor = valor % Decimal(0.05)

print('Valor: ', valor)
moedas_1_centavo = int(valor / Decimal(0.01))
print('Moedas de 0.01: ', moedas_1_centavo)

valor = valor % Decimal(0.01)

print('valor restante: ', valor)

