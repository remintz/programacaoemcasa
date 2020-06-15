"""
Altere sua solução do exercício 3 da lista da Aula 2 criando uma função 
que calcule e retorne o valor do imposto de renda a partir do valor de 
um salário que é passado a esta função como parâmetro.
"""
def irpf(salario):
    ir = 0.0
    if salario <= 1903.98:
        ir = 0.0
    elif salario > 1903.98 and salario <= 2862.65:
        ir = salario * 0.075 - 142.80
    elif salario > 2862.65 and salario <= 3751.05:
        ir = salario * 0.15 - 354.80
    elif salario > 3751.05 and salario <= 4664.68:
        ir = salario * 0.225 - 636.13
    else:
        ir = salario * 0.275 - 869.36
    return ir



salario = float(input('Qual é o valor do salário? '))

print(f'Para o salario de {salario:.2f} o IRRF é {irpf(salario):.2f}')
