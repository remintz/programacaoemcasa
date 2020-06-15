"""
Faça um programa com uma função que necessite um argumento (parâmetro)
e que retorna o valor 1 se o número passado como parâmetro for positivo, 
-1 se for negativo ou 0 (zero) se for zero
"""
def sinal(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0

n = 5
print(f'O sinal de {n} é {sinal(n)}')


n = -10
print(f'O sinal de {n} é {sinal(n)}')


n = 0
print(f'O sinal de {n} é {sinal(n)}')


n = 999
print(f'O sinal de {n} é {sinal(n)}')
