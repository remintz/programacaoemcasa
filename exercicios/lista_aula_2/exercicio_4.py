"""
(Exercício de while ou for) Faça um programa que leia 3 números usando input e mostre a soma e a média deles.
"""
soma = 0.0
for i in range(3):
    numero = float(input(f'Informe o número {i+1}: '))
    soma = soma + numero
print(f'A soma é {soma}')
print(f'A média é {soma / 3}')
