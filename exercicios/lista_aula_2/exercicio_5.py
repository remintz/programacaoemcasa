"""
(Exercício de while ou for) Faça um programa que receba dois números inteiros e gere
os números inteiros que estão no intervalo compreendido por eles.
"""
primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

if primeiro > segundo:
    # troca a ordem
    aux = primeiro
    primeiro = segundo
    segundo = aux

for i in range(primeiro + 1, segundo):
    print(i)
    