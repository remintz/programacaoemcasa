resultados = [
    ['+', '+', '+', ' ', ' ', ' ', ' ', ' ', ' ' ],
    [' ', ' ', ' ', '+', '+', '+', ' ', ' ', ' ' ],
    [' ', ' ', ' ', ' ', ' ', ' ', '+', '+', '+' ],
    ['+', ' ', ' ', '+', ' ', ' ', '+', ' ', ' ' ],
    [' ', '+', ' ', ' ', '+', ' ', ' ', '+', ' ' ],
    [' ', ' ', '+', ' ', ' ', '+', ' ', ' ', '+' ],
    ['+', ' ', ' ', ' ', '+', ' ', ' ', ' ', '+' ],
    [' ', ' ', '+', ' ', '+', ' ', '+', ' ', ' ' ]
]

def ve_se_ganhou(status, jogador):
    tab = status.copy()
    for i in range(9):
        if tab[i] == jogador:
            tab[i] = '+'
        else:
            tab[i] = ' '

    for i in range(len(resultados)):
        if tab == resultados[i]:
            return resultados[i]
            
    return None

def deu_velha(status):
    for i in range(9):
        if status[i] == ' ':
            return False
    return True

