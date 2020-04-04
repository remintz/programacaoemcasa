perguntas = {
    1: {
        'questao': 'O animal que você pensou tem 4 patas',
        True: {
            'indice_pergunta': None,
            'animal': 'cachorro'
        },
        False: {
            'animal': 'periquito',
            'indice_pergunta': None
        }
    }
}

def formula_pergunta(questao):
    continua = True
    while continua:
        resp = input('%s? (s/n)' % questao)
        if resp in "sSnN":
            return resp.upper() == 'S'

total_perguntas = 1
joga_novamente = True
while joga_novamente:
    continua = True
    num_pergunta = 1
    while continua:
        print(perguntas)
        pergunta = perguntas[num_pergunta]
        # faz uma pergunta sobre o animal e aguarda a resposta
        resp = formula_pergunta(pergunta['questao'])
        print('resp: ', resp)
        if pergunta[resp]['indice_pergunta'] is not None:
            # se a alternativa tem um indice para outra pergunta volta
            num_pergunta = pergunta[resp]['indice_pergunta']
        else:
            # se a alternativa já tem um animal fala ele e pede confirmacao
            computador_acertou = formula_pergunta('O animal é %s' % pergunta[resp]['animal'])
            # se o computador acertou... acabou...
            if computador_acertou:
                print('Acertei')
                continua = False
            # se o computador errou...
            else:
                # pergunta o nome do animal e qual seria a pergunta para diferenciar 
                total_perguntas += 1
                nome_animal = input('Não sei qual é o animal. Qual é o nome dele? ')
                nova_pergunta = input('Qual pergunta (s/n) teria que fazer para identificar este animal? ')
                # armazena a nova pergunta... o animal que foi o chute errado vai para o nao
                nova_pergunta = {
                    'questao': nova_pergunta
                }
                nova_pergunta[False] = {}
                nova_pergunta[True] = {}

                nova_pergunta[False]['animal'] = pergunta[resp]['animal']
                nova_pergunta[False]['indice_pergunta'] = None

                nova_pergunta[True]['animal'] = nome_animal
                nova_pergunta[True]['indice_pergunta'] = None

                perguntas[total_perguntas] = nova_pergunta

                pergunta[resp]['animal'] = None
                pergunta[resp]['indice_pergunta'] = total_perguntas

                print('Perdi')
                continua = False
                # o computador perdeu... acabou
