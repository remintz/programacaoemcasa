"""
(Exercício de if) Faça um programa que, dados três números quaisquer, A, B e C mostre e mostre o maior e o menor deles. Faça o teste com os seguintes dados:
    • A=1,B=2,C=3
    • A=3,B=2,C=1
    • A=0,B=0,C=0
    • A=1,B=1,C=2
    • A=-2,B=-1,C=0
"""

# Para o teste com cada uma das alternativas retire o '#' da frente da linha que deseja usar como teste

# A = 1; B = 2; C = 3
# A = 3; B = 2; C = 1
# A = 0; B = 0; C = 0
# A = 1; B = 1; C = 2
A = -2; B = -1; C = 0

maior = 0
menor = 0

if A >= B >= C:
    maior = A
    menor = C
elif C >= A >= B:
    maior = C
    menor = B
elif B >= C >= A:
    maior = B
    menor = A
elif B >= A >= C:
    maior = B
    menor = C
elif C >= B >= A:
    maior = C
    menor = A
elif A >= C >= B:
    maior = A
    menor = B
else:
    print(f'Faltou este caso: A = {A}, B = {B}, C = {C}')
print(f'O número maior é {maior} e o menor é {menor}')
