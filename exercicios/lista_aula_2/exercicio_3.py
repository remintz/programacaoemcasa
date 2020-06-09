"""
(Exercício de if). Faça um programa para calcular o imposto de renda retido na fonte de acordo com o valor do salário, considerando que:
    Valor do Salário (R$)       Alíquota(%)     Parcela a deduzir(R$)
    Até 1.903,98                isento          isento
    De 1.903,99 até 2.826,65    7,5             142,80
    De 2.826,66 até 3.751,05    15              354,80
    De 3.751,06 até 4.664,68    22,5            636,13
    Acima de 4.664,68           27,5            869,36

    Exemplo: Para um salário de R$3.800,00 o IR será 3.800,00 x 22,5% - 636,13 = 218,87
"""
ir = 0.0
salario = float(input('Qual é o valor do salário? '))
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
print(f'Para o salario de {salario:.2f} o IRRF é {ir:.2f}')
