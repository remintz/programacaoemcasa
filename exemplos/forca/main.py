
forcas = [
"""    
=====+
     |
    
    
   
    
    
""",
"""    
=====+
     |
    ( )
     
   
     
    
""",
"""    
=====+
     |
    ( )
     - 
   
     

""",
"""    
=====+
     |
    ( )
     - 
     | 
     |
    
""",
"""    
=====+
     |
    ( )
     - 
   / |
     |
    
""",
"""    
=====+
     |
    ( )
     - 
   / | \\
     |
    
""",
"""    
=====+
     |
    ( )
     - 
   / | \\
     |
    / 
""",
"""    
=====+
     |
    ( )
     - 
   / | \\
     |
    / \\
""",
]


pedacos_na_forca = 0
letras_ja_escolhidas = ''

def exibe_forca(pedacos):
    print(forcas[pedacos])

def exibe_palavra_incompleta(palavra_completa, letras_ja_escolhidas):
    palavra_incompleta = ''
    for letra in palavra_completa:
        if letra in letras_ja_escolhidas:
            palavra_incompleta = palavra_incompleta + letra + ' '
        else:
            palavra_incompleta = palavra_incompleta + '_ '
    print('Palavra: ', palavra_incompleta)

def tem_a_letra_na_palavra(letra, palavra_completa):
    return letra in palavra_completa


palavra_completa = input('Escolha uma palavra complicada e não fale pro seu adversário: ')
continua = True
while continua:
    letra = input('Escolha uma letra: ')
    if letra in letras_ja_escolhidas:
        print('Esta letra já foi escolhida')
        continue
    if tem_a_letra_na_palavra(letra, palavra_completa):
        print('Muito bem! A palavra secreta tem a letra escolhida!')
    else:
        pedacos_na_forca += 1
        exibe_forca(pedacos_na_forca-1)
        if pedacos_na_forca > 7:
            print('MORREU!!!')
            break
        else:
            print('Ops! Mais um pedaço na forca!')
    letras_ja_escolhidas += letra
    exibe_palavra_incompleta(palavra_completa, letras_ja_escolhidas)
    print('Letras já escolhidas: ', letras_ja_escolhidas)
