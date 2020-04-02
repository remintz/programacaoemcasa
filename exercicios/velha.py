
FECHAMENTOS = [
        [
            ['@', '@', '@'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ],
        [
            [' ', ' ', ' '],
            ['@', '@', '@'],
            [' ', ' ', ' ']
        ],
        [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            ['@', '@', '@']
        ],
        [
            ['@', ' ', ' '],
            [' ', '@', ' '],
            [' ', ' ', '@']
        ],
        [
            [' ', ' ', '@'],
            [' ', '@', ' '],
            ['@', ' ', ' ']
        ],
        [
            ['@', ' ', ' '],
            ['@', ' ', ' '],
            ['@', ' ', ' ']
        ],
        [
            [' ', '@', ' '],
            [' ', '@', ' '],
            [' ', '@', ' ']
        ],
        [
            [' ', ' ', '@'],
            [' ', ' ', '@'],
            [' ', ' ', '@']
        ],
    ]

def ganhou(jogador, tabuleiro):
    for f in range(len(FECHAMENTOS)):
        # para cada possibilidade de fechamento
        fechamento = FECHAMENTOS[f]
        abandona = False
        for i in range(3):
            for j in range(3):
                if fechamento[i][j] == '@':
                    if tabuleiro[i][j] == jogador:
                        continue
                    else:
                        abandona = True
                        break
            # já sabe que não é
            if abandona:
                break
        if not abandona:
            # foi até o fim de uma possibilidade sem abandonar... ganhou
            return True
    return False

def pergunta_jogada(jogador, tabuleiro):
    invalida = True
    while invalida:
        jogada = input('Jogador %s: qual é a sua jogada (linha, coluna)? ' % jogador)
        coords = jogada.split(',')
        if len(coords) == 2:
            linha = int(coords[0])
            coluna = int(coords[1])
            if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
                if pode_colocar(linha, coluna, tabuleiro):
                    return linha, coluna
        print('jogada invalida')

def pode_colocar(linha, coluna, tabuleiro):
    return tabuleiro[linha][coluna] == ' '

def imprime_tabuleiro(tabuleiro):
    print()
    print(' %s | %s | %s' % (tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print('---+---+---')
    print(' %s | %s | %s' % (tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print('---+---+---')
    print(' %s | %s | %s' % (tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))
    print()

tab = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
for i in range(3):
    for j in range(3):
        tab[i][j] = ' '
jogador_da_vez = 'O'
continua = True
while continua:
    if jogador_da_vez == 'X':
        jogador_da_vez = 'O'
    else:
        jogador_da_vez = 'X'
    imprime_tabuleiro(tab)
    linha, coluna = pergunta_jogada(jogador_da_vez, tab)
    tab[linha][coluna] = jogador_da_vez
    if ganhou(jogador_da_vez, tab):
        imprime_tabuleiro(tab)
        print('%s GANHOU!' % jogador_da_vez)
        continua = False

