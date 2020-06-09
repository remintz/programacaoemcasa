'''
Dada a lista de nomes de gatos abaixo, faça um programa em Python que
informe quais nomes aparecem mais de uma vez, sem usar a função count()
'''

gatos = ['Coco', 'Princess', 'Cali', 'Sammy', 'Abby', 'Gizmo', 'Lilly', 'Sammy', 'Pumpkin', 'Cali', 'Abby', 'Cali', 'Luna', 'Boo']

unicos = []
repetidos = []
for gato in gatos:
    if gato not in unicos:
        unicos.append(gato)
    elif gato not in repetidos:
        print(f'O gato {gato} aparece mais de uma vez')
        repetidos.append(gato)
