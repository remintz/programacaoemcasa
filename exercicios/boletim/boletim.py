notas = [{'nome': 'Sophia Ahart', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 55, 'portugues': 70, 'ciencias': 95, 'historia': 95, 'geografia': 60, 'ingles': 75}}, {'trimestre': 2, 'disciplinas': {'matematica': 90, 'portugues': 85, 'ciencias': 95, 'historia': 65, 'geografia': 90, 'ingles': 55}}, {'trimestre': 3, 'disciplinas': {'matematica': 50, 'portugues': 70, 'ciencias': 55, 'historia': 65, 'geografia': 90, 'ingles': 80}}]}, {'nome': 'Michael Tobias', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 90, 'portugues': 80, 'ciencias': 80, 'historia': 50, 'geografia': 60, 'ingles': 90}}, {'trimestre': 2, 'disciplinas': {'matematica': 85, 'portugues': 65, 'ciencias': 90, 'historia': 55, 'geografia': 90, 'ingles': 85}}, {'trimestre': 3, 'disciplinas': {'matematica': 90, 'portugues': 75, 'ciencias': 85, 'historia': 75, 'geografia': 50, 'ingles': 65}}]}, {'nome': 'Paul Asakura', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 85, 'portugues': 50, 'ciencias': 75, 'historia': 90, 'geografia': 90, 'ingles': 60}}, {'trimestre': 2, 'disciplinas': {'matematica': 55, 'portugues': 80, 'ciencias': 55, 'historia': 95, 'geografia': 70, 'ingles': 50}}, {'trimestre': 3, 'disciplinas': {'matematica': 75, 'portugues': 50, 'ciencias': 95, 'historia': 75, 'geografia': 80, 'ingles': 90}}]}, {'nome': 'Leon Mcthay', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 65, 'portugues': 60, 'ciencias': 80, 'historia': 50, 'geografia': 65, 'ingles': 85}}, {'trimestre': 2, 'disciplinas': {'matematica': 75, 'portugues': 95, 'ciencias': 50, 'historia': 65, 'geografia': 60, 'ingles': 70}}, {'trimestre': 3, 'disciplinas': {'matematica': 55, 'portugues': 75, 'ciencias': 75, 'historia': 55, 'geografia': 95, 'ingles': 60}}]}, {'nome': 'Linda Flowers', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 50, 'portugues': 65, 'ciencias': 80, 'historia': 60, 'geografia': 90, 'ingles': 80}}, {'trimestre': 2, 'disciplinas': {'matematica': 50, 'portugues': 50, 'ciencias': 90, 'historia': 85, 'geografia': 80, 'ingles': 80}}, {'trimestre': 3, 'disciplinas': {'matematica': 55, 'portugues': 70, 'ciencias': 60, 'historia': 65, 'geografia': 55, 'ingles': 95}}]}, {'nome': 'Jonathan Smith', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 50, 'portugues': 60, 'ciencias': 60, 'historia': 90, 'geografia': 90, 'ingles': 80}}, {'trimestre': 2, 'disciplinas': {'matematica': 70, 'portugues': 80, 'ciencias': 85, 'historia': 85, 'geografia': 65, 'ingles': 95}}, {'trimestre': 3, 'disciplinas': {'matematica': 90, 'portugues': 55, 'ciencias': 90, 'historia': 60, 'geografia': 90, 'ingles': 65}}]}, {'nome': 'Carlos Russo', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 75, 'portugues': 80, 'ciencias': 95, 'historia': 60, 'geografia': 80, 'ingles': 50}}, {'trimestre': 2, 'disciplinas': {'matematica': 75, 'portugues': 85, 'ciencias': 55, 'historia': 80, 'geografia': 85, 'ingles': 55}}, {'trimestre': 3, 'disciplinas': {'matematica': 95, 'portugues': 60, 'ciencias': 95, 'historia': 70, 'geografia': 85, 'ingles': 80}}]}, {'nome': 'Vita Smith', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 70, 'portugues': 60, 'ciencias': 90, 'historia': 60, 'geografia': 55, 'ingles': 60}}, {'trimestre': 2, 'disciplinas': {'matematica': 55, 'portugues': 95, 'ciencias': 75, 'historia': 80, 'geografia': 70, 'ingles': 85}}, {'trimestre': 3, 'disciplinas': {'matematica': 70, 'portugues': 90, 'ciencias': 75, 'historia': 75, 'geografia': 70, 'ingles': 75}}]}, {'nome': 'Joyce Sabb', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 95, 'portugues': 80, 'ciencias': 60, 'historia': 60, 'geografia': 65, 'ingles': 50}}, {'trimestre': 2, 'disciplinas': {'matematica': 50, 'portugues': 85, 'ciencias': 90, 'historia': 75, 'geografia': 95, 'ingles': 95}}, {'trimestre': 3, 'disciplinas': {'matematica': 85, 'portugues': 95, 'ciencias': 50, 'historia': 65, 'geografia': 55, 'ingles': 65}}]}, {'nome': 'Ernest Broussard', 'boletim': [{'trimestre': 1, 'disciplinas': {'matematica': 70, 'portugues': 85, 'ciencias': 80, 'historia': 60, 'geografia': 65, 'ingles': 55}}, {'trimestre': 2, 'disciplinas': {'matematica': 50, 'portugues': 55, 'ciencias': 75, 'historia': 85, 'geografia': 65, 'ingles': 50}}, {'trimestre': 3, 'disciplinas': {'matematica': 95, 'portugues': 90, 'ciencias': 95, 'historia': 60, 'geografia': 75, 'ingles': 90}}]}]

def descobre_disciplinas(notas):
    # descobre o nome das disciplinas que existem no boletim
    # considera que as do primeiro aluno são as mesmas para todos
    aluno = notas[0]
    boletim = aluno['boletim']
    disciplinas = boletim[0]['disciplinas']
    return list(disciplinas.keys())

def imprime_disciplina(nome_aluno, nome_disciplina, notas):
    # notas contém uma lista com as notas de cada um dos 3 trimestres
    linha = '%-20s | %-14s |' % (nome_aluno, nome_disciplina)
    soma_notas = 0 # para calcular a média
    for nota in notas:
        linha += '     %2d    |' % nota
        soma_notas += nota
    media = soma_notas / len(notas)
    linha += '    %2.0f     |' % media
    if media >= 70:
        linha += ' Aprovado'
    else:
        linha += ' Reprovado'
    print(linha)



disciplinas = descobre_disciplinas(notas)

# imprime o cabeçalho
print('Nome do Aluno        |  Disciplina    | Trim. 1   |  Trim. 2  |  Trim. 3  |   Média     |  Situacao')
print('---------------------+----------------|-----------|-----------|-----------|-----------|--------------')

for aluno in notas:
    nome_aluno = aluno['nome']
    boletim = aluno['boletim']
    mostra_nome_do_aluno = True
    for disciplina in disciplinas:
        nota_trimestre = []
        for indice_trimestre in range(3):
            nota_trimestre.append(boletim[indice_trimestre]['disciplinas'][disciplina])
        if mostra_nome_do_aluno:
            mostra_nome_do_aluno = False
        else:
            nome_aluno = ''
        imprime_disciplina(nome_aluno, disciplina, nota_trimestre)
    print('---------------------+----------------|-----------|-----------|-----------|-----------|--------------')
