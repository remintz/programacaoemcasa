"""
(Exercício de if) Faça um programa para a leitura uma nota de um aluno entre 0 e 10. Dependendo da nota o programa deve apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
• A mensagem "Reprovado", se a média for menor do que sete;
• A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota = float(input('Qual é a nota do aluno? '))
if nota < 0 or nota > 10:
    print('Nota inválida')
elif nota == 10:
    print('Aprovado com Distinção')
elif nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')