from getname import random_name

# def estrelas(num):
#   linha = ''
#   for i in range(num):
#     linha = linha + '*'
#   return linha

#gerar N nomes aleatorios de gatos e guardar no arquivo 'cats.txt'
f = open('cats.txt', 'w')
for i in range(100):
  cat = random_name('cat')
  print(cat)


# ler o arquivo 'cats.txt' e colocar o conteudo em uma lista de nomes de gatos
f = open('cats.txt')
cats = f.read().splitlines()

# count = {}
# for cat in cats:
#   if cat in count:
#     count[cat] = count[cat] + 1
#   else:
#     count[cat] = 1
# print (count)

# print(cats)
num_nao_repetidos = 0
for i in range(len(cats)):
  repetido = False
  for j in range(i+1, len(cats)):
    if cats[i] == cats[j]:
      # print("O nome %s está repetido" % cats[i])
      repetido = True
  if not repetido:
    print("O nome %s não está repetido" % cats[i])
    num_nao_repetidos = num_nao_repetidos + 1
# for cat in count.keys():
#   print('%10s %s' % (cat, estrelas(count[cat])))


print('Número de não repetidos: %d' % num_nao_repetidos)
# mostrar quais são os nomes que aparecem mais de uma vez na lista


