"""
(Exercício de while ou for) Imprima uma tabela de conversão de temperatura de graus Celsius para graus Farenheit,
começando de -10oC até 50oC, de meio em meio grau, sabendo que:
    Graus Farenheit = Graus Celsius * 1.8 + 32
"""
inicio = -10.0
fim = 50.0

graus_c = inicio
print(f'|{"graus C":^10}|{"graus F":^10}|')
print('+----------+----------+')
while graus_c <= fim:
    print(f'|{graus_c:10.1f}|{(graus_c * 1.8 + 32):10.1f}|')
    graus_c = graus_c + 0.5
print('+----------+----------+')
