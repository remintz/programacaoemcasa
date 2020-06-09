'''
(listas e comando ‘for’) Dadas duas listas: a = [1, 6, 4, 8, 3, 9, 89, 54, 3, 5]
b = [5, 9, 1, 4, 8, 66, 44, 33, 3]
a) Construa uma lista intersecao que contenha os elementos comuns às duas listas
b) Construa uma lista uniao que contenha a todos os membros das duas listas
c) Construa uma lista intersecao_a_e_nao_b com os elementos da lista a que não
aparecem na lista b
'''

a = [1, 6, 4, 8, 3, 9, 89, 54, 3, 5]
b = [5, 9, 1, 4, 8, 66, 44, 33, 3]

# letra a
intersecao = []
for item_a in a:
    # percorrendo cada elemento da lista a
    if item_a in b:
        # este elemento está nas duas listas
        if not item_a in intersecao:
            # evitando elementos repetidos
            intersecao.append(item_a)
print(f'Interseção entre a e b: {intersecao}')

# letra b
uniao = []
for item_a in a:
    if not item_a in uniao:
        uniao.append(item_a)
for item_b in b:
    if not item_b in uniao:
        uniao.append(item_b)

print(f'Uniao entre a e b: {uniao}')

# letra c
intersecao_a_e_nao_b = []
for item_a in a:
    if not item_a in b:
        if not item_a in intersecao_a_e_nao_b:
            intersecao_a_e_nao_b.append(item_a)
print(f'Elementos de a que não estão em b: {intersecao_a_e_nao_b}')
