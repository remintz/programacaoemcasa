import random

def gera_questao(nome_estado, opcoes):
    q = """Qual é a capital do estado %s?

    Opções:
        A) %s
        B) %s
        C) %s
        D) %s
    """
    return q % (nome_estado, opcoes[0], opcoes[1], opcoes[2], opcoes[3])

def gera_gabarito(questoes):
    gabarito = ''
    for i in range(len(questoes)):
        num_questao = i + 1
        resposta = questoes[i]
        gabarito += "%s - %s\n" % (num_questao, resposta)
    return gabarito

def sorteia_capitais(numero, capitais, capital_correta):
    print(capitais)
    print(capital_correta)
    sorteadas = [capital_correta]
    capitais.remove(capital_correta)
    for i in range(numero-1):
        sorteada = random.choice(capitais)
        sorteadas.append(sorteada)
        capitais.remove(sorteada)
    random.shuffle(sorteadas)
    correta = sorteadas.index(capital_correta)
    return sorteadas, correta        

# ler estados
f_estados = open('exercicios/estados.csv')
estados = f_estados.readlines()
lista_estados = []
lista_capitais = []
for estado in estados:
    campos_estado = estado.replace('\n', '').split(',')
    e = {
        'sigla': campos_estado[0],
        'nome': campos_estado[1],
        'capital': campos_estado[2]
    }
    lista_estados.append(e)
    lista_capitais.append(campos_estado[2])

# gera questão
gabarito = []
questoes = random.sample(lista_estados, 5)
for i in range(5):
    estado = questoes[i]
    print(estado)
    opcoes, correta = sorteia_capitais(4, lista_capitais, estado['capital'])
    q = gera_questao(estado['nome'], opcoes)
    print(q)
    gabarito.append(correta + 1)
    with open('exercicios/questao_%s.txt' % str(i+1), 'w') as f:
        f.write(q)
with open('exercicios/gabarito.txt', 'w') as f:
    f.write(gabarito)

