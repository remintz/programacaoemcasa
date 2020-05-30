from guizero import App, Window, Text, Box, PushButton
import time

from veseganhou import ve_se_ganhou, deu_velha

status = [' '] * 9
jogador = 'X'
buttons = []
cabecalho = None
jogando = True

def colore_resultado(resultado):
    for i in range(9):
        if resultado[i] == '+':
            buttons[i].text_color = 'red'
        else:
            buttons[i].enabled = False

def button_clicked(contador):
    global jogador
    global jogando

    if not jogando:
        return
    if status[contador] == ' ':
        status[contador] = jogador
        buttons[contador].text = jogador
        if deu_velha(status):
            cabecalho.value = 'Deu velha!'
            jogando=False
            return
        resultado = ve_se_ganhou(status, jogador)
        if resultado is not None:
            colore_resultado(resultado)
            cabecalho.value = 'O %s venceu!' % jogador
            jogando = False
        else:
            if jogador == 'X':
                jogador = 'O'
            else:
                jogador = 'X'
            cabecalho.value = 'Quem joga é o %s' % jogador

if __name__ == '__main__':
    app = App()
    cabecalho = Text(app, text='Quem joga é o %s' % jogador, size=20)
    tabuleiro = Box(app, layout='grid')
    contador = 0
    for i in range(3):
        for j in range(3):
            button = PushButton(tabuleiro, text=' ', grid=[i, j], width=10, height=6, command=button_clicked, args=[contador])
            contador += 1
            buttons.append(button)
    app.display()

