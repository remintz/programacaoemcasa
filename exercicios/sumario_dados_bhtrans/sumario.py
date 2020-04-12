f = open('acidentes-bh-2018.csv')
dados = f.readlines()
contador = {}
for dado in dados:
    ocorrencia = dado.split(';')
    logradouro = ocorrencia[7].strip()
    contador[logradouro] =  contador.get(logradouro, 0) + 1

saida = open('acidentes-bh-2018-por-logradouro.csv', 'w')
for c in contador:
    saida.write(c + ';' + str(contador[c]) + '\n')
saida.close()