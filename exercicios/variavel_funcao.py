def funcao_renato():
    return 'Renato'

def funcao_carlos():
    return 'Carlos'

def imprime_ola(funcao):
    print('Ola ' + funcao())

f = funcao_renato
# f = funcao_carlos

imprime_ola(f)
