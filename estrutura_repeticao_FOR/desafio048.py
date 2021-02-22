
#  Faça um programa que calcule a:

    # Soma entre todos os NÚMEROS ÍMPARES

    # Que são MÚLTIPLOS DE 3

    # e que se encontram no intervalor de 1 até 500

soma = 0
contador = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num   # um acumulador normalmente soma um valor
        contador += 1 # um contador normalmente soma 1
        
print(soma)
print(contador)
print('fim')