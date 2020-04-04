def classifica_imc(imc):
    classificacao = None
    if imc < 18.5:
        classificacao = 'Magreza'
    elif 18.5 <= imc < 25:
        classificacao = 'Normal'
    elif 25 <= imc < 30:
        classificacao = 'Sobrepeso'
    elif 30 <= imc < 40:
        classificacao = 'Obesidade'
    else:
        classificacao = 'Obesidade Grave'
    return classificacao


peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura (em metros)? '))

imc = peso / altura ** 2
print('seu IMC é %s (%s)' % (imc, classifica_imc(imc)))

