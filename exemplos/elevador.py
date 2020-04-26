class Elevador:
    def __init__(self, andares):
        self._andares = andares
        self._andar_atual = 1
        self._estado = 'parado'
        self._andar_selecionado = None

    def get_andar_atual(self):
        return self._andar_atual

    def get_estado(self):
        return self._estado

    def seleciona_andar(self, andar):
        if self._estado == 'parado':
            self._andar_selecionado = andar
            if self._andar_atual > self._andar_selecionado:
                self._estado = 'descendo'
            elif self._andar_atual < self._andar_selecionado:
                self._estado = 'subindo'
            else:
                self._estado = 'parado'
                self._andar_selecionado = None
        else:
            print('Este elevador só atende uma pessoa de cada vez')

    def motor(self):
        if self._estado == 'subindo':
            if self._andar_atual < self._andares:
                self._andar_atual += 1
                if self._andar_atual == self._andar_selecionado:
                    self._chegou()
            else:
                self._chegou()
        elif self._estado == 'descendo':
            if self._andar_atual > 1:
                self._andar_atual -= 1
                if self._andar_atual == self._andar_selecionado:
                    self._chegou()
            else:
                self._chegou()

    def _chegou(self):
        self._estado = 'parado'
        self._andar_selecionado = None
        print('chegou no andar %d' % self._andar_atual)


e = Elevador(10)
andar = int(input('Informe o andar: '))
while (andar > 0):
    e.seleciona_andar(andar)
    estado = e.get_estado()
    print(estado)
    andando = True
    while andando:
        e.motor()
        andar = e.get_andar_atual()
        estado = e.get_estado()
        print('o elevador está no andar %d e está %s' % (andar, estado))
        andando = estado != 'parado'
    andar = int(input('Informe o andar: '))