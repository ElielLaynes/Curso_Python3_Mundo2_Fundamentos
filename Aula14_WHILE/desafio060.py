
# Faça um programa que leia um número qualquer

# Mostre na tela o seu FATORIAL

# Ex:. 5! = 5 x 4 x 3 x 2 x 1 = 120



# Opção utilizando O pacoto Math e a Função factorial
'''
from math import factorial

num = int ( input ( 'Digite um Número: ' ) )

fat = factorial(num)
print(f'O fatorial de {num} é: {fat}')'''





num = int ( input ( 'Digite um Número: ' ) )
cont = num

fat = 1

print('Calculando {num}! ', end='')

while cont > 0:

    print(f'{cont}', end='')

    print(' x ' if cont > 1 else ' = ', end='')

    fat *= cont

    cont -= 1

print(f'{fat} \n' , end='')