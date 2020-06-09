'''
    Crie uma lista com os ‘n’ primeiros números primos, 
    onde o valor de ‘n’ é informado pelo usuário. Lembrando que os 
    números primos são aqueles que só são divisíveis por eles mesmos
    e por 1.
'''

quantos = int(input('Quantos números primos você quer? '))

contador_de_primos = 0
dividendo = 0

while contador_de_primos < quantos:
    dividendo = dividendo + 1
    # print(f'Vendo se {dividendo} é primo')
    eh_primo = True
    for divisor in range(2, dividendo):
        # print(f'testando o divisor {divisor}')
        resto = dividendo % divisor
        if resto == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f'{contador_de_primos+1}: {dividendo}')
        contador_de_primos = contador_de_primos + 1
    


