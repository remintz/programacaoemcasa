from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout


jogador = 'X'


def build_screen():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    cabecalho = QVBoxLayout()
    label = QLabel('Quem joga é o %s' % jogador)
    cabecalho.addWidget(label)
    layout.addLayout(cabecalho)

    tabuleiro = QGridLayout()

    buttons = []
    for i in range(3):
        columns = []
        for j in range(3):
            button = QPushButton('X')
            tabuleiro.addWidget(button, i, j)
            columns.append(button)
        buttons.append(columns)
    layout.addLayout(tabuleiro)

    window.setLayout(layout)
    window.show()
    app.exec_()

build_screen()
