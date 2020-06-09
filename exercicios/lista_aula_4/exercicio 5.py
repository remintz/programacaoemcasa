'''
(dicionarios e listas) Dada a lista de dicionários abaixo:
Notas = [ # cada indice da lista corresponde a um trimestre
{ 'ciencias': 80, 'ingles': 55, 'matematica': 70, 'portugues': 85 }, # trimestre 1 
{ 'ciencias': 90, 'ingles': 75, 'matematica': 74, 'portugues': 75 }, # trimestre 2 
{ 'ciencias': 85, 'ingles': 85, 'matematica': 30, 'portugues': 55 } # trimestre 3
]
Faça um programa em Python que imprima:
a) A nota de português do 2.o trimestre
b) A nota de matemática do 1.o trimestre
c) A média das notas de ciências
d) O trimestre com a maior nota de inglês
'''


Notas = [ # cada indice da lista corresponde a um trimestre
{ 'ciencias': 80, 'ingles': 55, 'matematica': 70, 'portugues': 85 }, # trimestre 1 
{ 'ciencias': 90, 'ingles': 75, 'matematica': 74, 'portugues': 75 }, # trimestre 2 
{ 'ciencias': 85, 'ingles': 85, 'matematica': 30, 'portugues': 55 } # trimestre 3
]

# letra a
print(f'A nota de português do 2.o trimestre: { Notas[1]["portugues"] }')

# letra b
print(f'A nota de matemática do 1.o trimestre: { Notas[0]["matematica"] }')

# letra c
soma = 0
for trimestre in Notas:
    soma = soma + trimestre['ciencias']
print(f'A média das notas de ciências é: {soma / len(Notas)}')

# letra d
notas_ingles = []
for trimestre in Notas:
    notas_ingles.append(trimestre['ingles'])
maior_nota_ingles = max(notas_ingles)
indice_trimestre_maior_nota = notas_ingles.index(maior_nota_ingles)
trimestre_maior_nota = indice_trimestre_maior_nota + 1

print(f'O trimestre com a maior nota de inglês é o {trimestre_maior_nota}')
