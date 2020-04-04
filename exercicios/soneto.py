soneto = """De repente do riso fez-se o pranto
Silencioso e branco como a bruma
E das bocas unidas fez-se a espuma
E das mãos espalmadas fez-se o espanto
De repente da calma fez-se o vento
Que dos olhos desfez a última chama
E da paixão fez-se o pressentimento
E do momento imóvel fez-se o drama
De repente não mais que de repente
Fez-se de triste o que se fez amante
E de sozinho o que se fez contente
Fez-se do amigo próximo distante
Fez-se da vida uma aventura errante
De repente não mais que de repente """

s = soneto.replace('\n', ' ')
s = s.split(' ')
contador = {}
for palavra in s:
    if contador.get(palavra) is None:
        contador[palavra] = 1
    else:
        contador[palavra] += 1
for palavra in contador:
    estrelas = '*' * contador[palavra]
    print("%20s - %s" % (palavra, estrelas))

