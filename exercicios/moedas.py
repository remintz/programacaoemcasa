valor = float(input('Qual é o valor em Reais? '))

notas_100 = int(valor / 100)
print('Notas de 100: ', notas_100)

valor = valor - notas_100 * 100

notas_50 = int(valor / 50)
print('Notas de 50: ', notas_50)

valor = valor - notas_50 * 50

notas_20 = int(valor / 20)
print('Notas de 20: ', notas_20)

valor = valor - notas_20 * 20

notas_10 = int(valor / 10)
print('Notas de 10: ', notas_10)

valor = valor - notas_10 * 10

notas_5 = int(valor / 5)
print('Notas de 5: ', notas_5)

valor = valor - notas_5 * 5

notas_2 = int(valor / 2)
print('Notas de 2: ', notas_2)

valor = valor - notas_2 * 2

moedas_1 = int(valor / 1)
print('Moedas de 1: ', moedas_1)

valor = valor - moedas_1

moedas_50 = int(valor / 0.50)
print('Moedas de 0.50: ', moedas_50)

valor = valor - moedas_50 * 0.5

moedas_25 = int(valor / 0.25)
print('Moedas de 0.25: ', moedas_25)

valor = valor - moedas_25 * 0.25

moedas_10 = int(valor / 0.10)
print('Moedas de 0.10: ', moedas_10)

valor = valor - moedas_10 * 0.1

moedas_5 = int(valor / 0.05)
print('Moedas de 0.05: ', moedas_5)

valor = valor - moedas_5 * 0.05

moedas_1_centavo = int(valor / 0.01)
print('Moedas de 0.01: ', moedas_1_centavo)

valor = valor - moedas_1_centavo * 0.01

print('valor restante: ', valor)

