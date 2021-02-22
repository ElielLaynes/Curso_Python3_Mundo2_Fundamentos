
# faça um programa que :

    # leia um número inteiro

    # Diga se ele é ou não um Número Primo
    # Números primos são os números divisíveis por 1 e por ele mesmo.


num = int ( input ( 'Digite um Número: ' ) )
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[33m' , end='')
        tot += 1
    else:
        print('\033[31m' , end='')
    print(n, end=' ')
print(num, tot)

if tot == 2:
    print('Primo')
else:
    print('Não é Primo')