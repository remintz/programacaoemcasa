peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura (em metros)? '))

imc = peso / altura ** 2
print('Seu IMC é: ', imc)
if imc < 18.5:
    print('Magreza')
elif 18.5 <= imc < 25:
    print('Normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Grave')
