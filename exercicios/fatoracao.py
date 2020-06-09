numero = float(input('Qual é o número? '))
if numero <= 0:
    print('O número deve ser maior que zero')
    exit()
if numero % 1 != 0:
    print('O número deve ser inteiro')
    exit()
numero_int = int(numero)
print(f'Os divisores de {numero_int} são: ')
for i in range(1, numero_int + 1):
    if numero % i == 0:
        print(i)
